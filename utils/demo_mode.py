"""
Demo Mode — generates a fake prediction so you can test the full UI
before the real model is trained.

Usage:
    from utils.demo_mode import demo_predict
    result = demo_predict(image)
"""

import random
import numpy as np
from PIL import Image

# All supported classes
DEMO_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Corn___Cercospora_leaf_spot",
    "Corn___Common_rust",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]


def demo_predict(image: Image.Image) -> dict:
    """
    Returns a simulated prediction result for UI testing.
    Picks a random class with a realistic confidence distribution.
    """
    # Pick a random top class
    top_class = random.choice(DEMO_CLASSES)

    # Generate realistic softmax-like probabilities
    raw = np.random.dirichlet(np.ones(len(DEMO_CLASSES)) * 0.3)
    # Boost the top class so it looks realistic
    top_idx = DEMO_CLASSES.index(top_class)
    raw[top_idx] += random.uniform(0.4, 0.7)
    raw = raw / raw.sum()

    confidence = float(raw[top_idx])

    # Build top-5
    sorted_idx = np.argsort(raw)[::-1][:5]
    top5 = {DEMO_CLASSES[i]: float(raw[i]) for i in sorted_idx}

    return {
        "class_name":     top_class,
        "confidence":     confidence,
        "top5":           top5,
        "low_confidence": confidence < 0.60,
        "demo":           True,
    }
