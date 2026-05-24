"""
Creates a small demo CNN model so the app works without training.
This model gives random predictions — for UI demonstration only.
Replace with the real trained model after running train_model.py.
"""

import os
import json
import numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

SAVE_DIR = os.path.dirname(__file__)

CLASS_NAMES = {
    0:  "Apple___Apple_scab",
    1:  "Apple___Black_rot",
    2:  "Apple___Cedar_apple_rust",
    3:  "Apple___healthy",
    4:  "Corn___Cercospora_leaf_spot",
    5:  "Corn___Common_rust",
    6:  "Corn___Northern_Leaf_Blight",
    7:  "Corn___healthy",
    8:  "Potato___Early_blight",
    9:  "Potato___Late_blight",
    10: "Potato___healthy",
    11: "Tomato___Bacterial_spot",
    12: "Tomato___Early_blight",
    13: "Tomato___Late_blight",
    14: "Tomato___Leaf_Mold",
    15: "Tomato___Septoria_leaf_spot",
    16: "Tomato___Spider_mites",
    17: "Tomato___Target_Spot",
    18: "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    19: "Tomato___Tomato_mosaic_virus",
    20: "Tomato___healthy",
}

NUM_CLASSES = len(CLASS_NAMES)

print("[INFO] Building demo CNN model...")

model = keras.Sequential([
    layers.Input(shape=(224, 224, 3)),

    layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),
    layers.Dropout(0.25),

    layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),
    layers.Dropout(0.25),

    layers.Conv2D(128, (3, 3), padding="same", activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),
    layers.Dropout(0.25),

    layers.Conv2D(256, (3, 3), padding="same", activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),
    layers.Dropout(0.25),

    layers.Conv2D(512, (3, 3), padding="same", activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dense(512, activation="relu"),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(NUM_CLASSES, activation="softmax"),
])

model.compile(
    optimizer="sgd",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# Save model
model_path = os.path.join(SAVE_DIR, "plant_disease_cnn.h5")
model.save(model_path)
print(f"\n[OK] Demo model saved to: {model_path}")

# Save class names
class_path = os.path.join(SAVE_DIR, "class_names.json")
with open(class_path, "w") as f:
    json.dump(CLASS_NAMES, f, indent=2)
print(f"[OK] Class names saved to: {class_path}")

print("\n[DONE] App will now load without errors.")
print("       NOTE: This demo model gives random predictions.")
print("       Train the real model with: python model/train_model.py")
