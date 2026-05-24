"""
Creates a small lightweight CNN model under 25MB for GitHub upload.
Uses GlobalAveragePooling instead of Flatten to reduce parameters.
"""
import os, json
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

SAVE_DIR = os.path.dirname(os.path.abspath(__file__))

CLASS_NAMES = {
    0:"Apple___Apple_scab", 1:"Apple___Black_rot", 2:"Apple___Cedar_apple_rust",
    3:"Apple___healthy", 4:"Corn___Cercospora_leaf_spot", 5:"Corn___Common_rust",
    6:"Corn___Northern_Leaf_Blight", 7:"Corn___healthy", 8:"Potato___Early_blight",
    9:"Potato___Late_blight", 10:"Potato___healthy", 11:"Tomato___Bacterial_spot",
    12:"Tomato___Early_blight", 13:"Tomato___Late_blight", 14:"Tomato___Leaf_Mold",
    15:"Tomato___Septoria_leaf_spot", 16:"Tomato___Spider_mites", 17:"Tomato___Target_Spot",
    18:"Tomato___Tomato_Yellow_Leaf_Curl_Virus", 19:"Tomato___Tomato_mosaic_virus",
    20:"Tomato___healthy"
}

print("[INFO] Building lightweight CNN model (target: <25MB)...")

model = keras.Sequential([
    layers.Input(shape=(224, 224, 3)),
    layers.Conv2D(16, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(32, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3,3), padding="same", activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(21, activation="softmax"),
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()

path = os.path.join(SAVE_DIR, "plant_disease_cnn.keras")
model.save(path)
size_mb = os.path.getsize(path) / (1024 * 1024)
print(f"\n[OK] Model saved: {path}")
print(f"[OK] Size: {size_mb:.2f} MB")

class_path = os.path.join(SAVE_DIR, "class_names.json")
with open(class_path, "w") as f:
    json.dump(CLASS_NAMES, f, indent=2)
print(f"[OK] Class names saved: {class_path}")
print("\n[DONE] Model is ready for GitHub upload.")
