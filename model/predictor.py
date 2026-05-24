"""
Prediction module — loads the trained CNN model and runs inference.
Implements the AI Analysis and Processing layer (Chapter 3.3 & 3.5).
"""

import os
import json
import numpy as np
from PIL import Image
import tensorflow as tf

# Paths
MODEL_PATH       = os.path.join(os.path.dirname(__file__), "plant_disease_cnn.h5")
CLASS_NAMES_PATH = os.path.join(os.path.dirname(__file__), "class_names.json")
IMG_SIZE         = (224, 224)

# Confidence threshold — below this triggers "Unrecognized Input" alert (Chapter 4.5)
CONFIDENCE_THRESHOLD = 0.60


class PlantDiseasePredictor:
    """
    Wraps the trained CNN model for inference.
    Implements the Adaptive Learning Feature described in Chapter 4.5.
    """

    def __init__(self):
        self.model = None
        self.class_names = {}
        self._load()

    def _load(self):
        """Load model and class names from disk."""
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Trained model not found at '{MODEL_PATH}'.\n"
                "Please run:  python model/train_model.py"
            )

        self.model = tf.keras.models.load_model(MODEL_PATH)

        if os.path.exists(CLASS_NAMES_PATH):
            with open(CLASS_NAMES_PATH, "r") as f:
                # Keys are strings from JSON; convert to int
                raw = json.load(f)
                self.class_names = {int(k): v for k, v in raw.items()}
        else:
            raise FileNotFoundError(
                f"Class names file not found at '{CLASS_NAMES_PATH}'.\n"
                "Please run:  python model/train_model.py"
            )

    def preprocess(self, image: Image.Image) -> np.ndarray:
        """
        Preprocessing pipeline (Chapter 4.3):
        - Resize to 224×224
        - Normalize pixel values to [0, 1]
        """
        img = image.convert("RGB")
        img = img.resize(IMG_SIZE, Image.LANCZOS)
        arr = np.array(img, dtype=np.float32) / 255.0   # Normalization
        arr = np.expand_dims(arr, axis=0)                # Add batch dimension
        return arr

    def predict(self, image: Image.Image) -> dict:
        """
        Run inference and return structured result.

        Returns:
            {
                "class_name":   str,   # e.g. "Tomato___Late_blight"
                "confidence":   float, # 0.0 – 1.0
                "all_probs":    dict,  # {class_name: probability}
                "low_confidence": bool # True if below threshold
            }
        """
        arr = self.preprocess(image)

        # Softmax probabilities (Chapter 2.1)
        probs = self.model.predict(arr, verbose=0)[0]

        top_idx        = int(np.argmax(probs))
        top_confidence = float(probs[top_idx])
        top_class      = self.class_names.get(top_idx, f"class_{top_idx}")

        # Build full probability map (top 5 for display)
        sorted_indices = np.argsort(probs)[::-1]
        top5 = {
            self.class_names.get(int(i), f"class_{i}"): float(probs[i])
            for i in sorted_indices[:5]
        }

        # Adaptive Learning Feature (Chapter 4.5)
        low_confidence = top_confidence < CONFIDENCE_THRESHOLD

        return {
            "class_name":     top_class,
            "confidence":     top_confidence,
            "top5":           top5,
            "low_confidence": low_confidence,
        }


# Singleton — loaded once, reused across Streamlit reruns
_predictor_instance = None


def get_predictor() -> PlantDiseasePredictor:
    global _predictor_instance
    if _predictor_instance is None:
        _predictor_instance = PlantDiseasePredictor()
    return _predictor_instance
