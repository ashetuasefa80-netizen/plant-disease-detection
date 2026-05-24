"""
Plant Disease Detection System
CNN Model Training Script
Author: Morketa Negash
University: Madda Walabu University
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
import matplotlib.pyplot as plt
import json

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────
IMG_SIZE    = (224, 224)   # Input size as described in Chapter 4
BATCH_SIZE  = 32
EPOCHS      = 30           # 30 epochs as stated in Chapter 4
LEARNING_RATE = 0.001      # Learning rate from Chapter 4
DATASET_DIR = "dataset"    # Folder containing PlantVillage images
MODEL_SAVE_PATH = "model/plant_disease_cnn.h5"

# Disease classes matching your document (Apple, Corn, Potato, Tomato)
CLASS_NAMES = [
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

NUM_CLASSES = len(CLASS_NAMES)


# ─────────────────────────────────────────────
#  DATA PREPROCESSING & AUGMENTATION (Chapter 4.3)
# ─────────────────────────────────────────────
def build_data_generators(dataset_dir):
    """
    Applies augmentation techniques described in Chapter 4.3:
    - Random rotation
    - Flipping
    - Brightness adjustment
    - Normalization (pixel values scaled to [0, 1])
    """
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,          # Normalization: scale to [0, 1]
        rotation_range=30,             # Random rotation
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,          # Flipping
        brightness_range=[0.8, 1.2],   # Brightness adjustment
        validation_split=0.2           # 80/20 train-val split
    )

    val_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        dataset_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True
    )

    val_generator = val_datagen.flow_from_directory(
        dataset_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False
    )

    return train_generator, val_generator


# ─────────────────────────────────────────────
#  CNN MODEL ARCHITECTURE (Chapter 4.4)
# ─────────────────────────────────────────────
def build_cnn_model(num_classes):
    """
    CNN architecture as described in Chapter 4.4:
    - 5 Convolutional layers
    - MaxPooling layers
    - Softmax output layer (Chapter 2.1)
    - Batch Normalization to prevent overfitting
    """
    model = keras.Sequential([
        # ── Input Layer ──
        layers.Input(shape=(224, 224, 3)),

        # ── Block 1: Conv → BN → ReLU → Pool ──
        layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        # ── Block 2 ──
        layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        # ── Block 3 ──
        layers.Conv2D(128, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.Conv2D(128, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        # ── Block 4 ──
        layers.Conv2D(256, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.Conv2D(256, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        # ── Block 5 ──
        layers.Conv2D(512, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.25),

        # ── Fully Connected Layers ──
        layers.Flatten(),
        layers.Dense(512, activation="relu"),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(256, activation="relu"),
        layers.Dropout(0.3),

        # ── Output Layer: Softmax (Chapter 2.1) ──
        layers.Dense(num_classes, activation="softmax"),
    ])

    return model


# ─────────────────────────────────────────────
#  TRAINING CALLBACKS
# ─────────────────────────────────────────────
def get_callbacks(model_save_path):
    """
    Callbacks to improve training:
    - ModelCheckpoint: saves the best model
    - EarlyStopping: stops if no improvement
    - ReduceLROnPlateau: reduces learning rate on plateau
    """
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)

    checkpoint = ModelCheckpoint(
        filepath=model_save_path,
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    )

    early_stop = EarlyStopping(
        monitor="val_accuracy",
        patience=7,
        restore_best_weights=True,
        verbose=1
    )

    reduce_lr = ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=3,
        min_lr=1e-6,
        verbose=1
    )

    return [checkpoint, early_stop, reduce_lr]


# ─────────────────────────────────────────────
#  PLOT TRAINING HISTORY (Figure 4.1)
# ─────────────────────────────────────────────
def plot_training_history(history, save_dir="model"):
    """Generates the Model Training Diagram referenced as Figure 4.1"""
    os.makedirs(save_dir, exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Model Training Results — Plant Disease Detection CNN", fontsize=14)

    # Accuracy plot
    axes[0].plot(history.history["accuracy"],     label="Train Accuracy", color="blue")
    axes[0].plot(history.history["val_accuracy"], label="Val Accuracy",   color="orange")
    axes[0].set_title("Model Accuracy")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")
    axes[0].legend()
    axes[0].grid(True)

    # Loss plot
    axes[1].plot(history.history["loss"],     label="Train Loss", color="blue")
    axes[1].plot(history.history["val_loss"], label="Val Loss",   color="orange")
    axes[1].set_title("Model Loss")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Loss")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    save_path = os.path.join(save_dir, "training_history.png")
    plt.savefig(save_path, dpi=150)
    print(f"[INFO] Training plot saved to: {save_path}")
    plt.show()


# ─────────────────────────────────────────────
#  SAVE CLASS NAMES
# ─────────────────────────────────────────────
def save_class_names(generator, save_dir="model"):
    """Saves class index mapping so the app can decode predictions."""
    os.makedirs(save_dir, exist_ok=True)
    # Invert the dict: index → class name
    class_indices = {v: k for k, v in generator.class_indices.items()}
    with open(os.path.join(save_dir, "class_names.json"), "w") as f:
        json.dump(class_indices, f, indent=2)
    print(f"[INFO] Class names saved. Total classes: {len(class_indices)}")
    return class_indices


# ─────────────────────────────────────────────
#  MAIN TRAINING PIPELINE
# ─────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  Plant Disease Detection System — CNN Training")
    print("  Madda Walabu University | Morketa Negash")
    print("=" * 60)

    # Check dataset exists
    if not os.path.exists(DATASET_DIR):
        print(f"\n[ERROR] Dataset folder '{DATASET_DIR}' not found.")
        print("  Please download the PlantVillage dataset and place it in:")
        print(f"  ./{DATASET_DIR}/ClassName/image.jpg")
        print("\n  Download: https://www.kaggle.com/datasets/emmarex/plantdisease")
        return

    # Build data generators
    print("\n[STEP 1] Loading and preprocessing dataset...")
    train_gen, val_gen = build_data_generators(DATASET_DIR)
    num_classes = len(train_gen.class_indices)
    print(f"  Found {num_classes} classes, {train_gen.samples} training images")

    # Save class names
    save_class_names(train_gen)

    # Build model
    print("\n[STEP 2] Building CNN model architecture...")
    model = build_cnn_model(num_classes)

    # Compile with SGDM optimizer (Chapter 4.4)
    optimizer = keras.optimizers.SGD(
        learning_rate=LEARNING_RATE,
        momentum=0.9,          # SGDM — Stochastic Gradient Descent with Momentum
        nesterov=True
    )

    model.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    model.summary()

    # Train
    print(f"\n[STEP 3] Training for up to {EPOCHS} epochs...")
    callbacks = get_callbacks(MODEL_SAVE_PATH)

    history = model.fit(
        train_gen,
        epochs=EPOCHS,
        validation_data=val_gen,
        callbacks=callbacks,
        verbose=1
    )

    # Evaluate
    print("\n[STEP 4] Evaluating on validation set...")
    val_loss, val_acc = model.evaluate(val_gen, verbose=0)
    print(f"\n  ✔ Validation Accuracy : {val_acc * 100:.2f}%")
    print(f"  ✔ Validation Loss     : {val_loss:.4f}")

    # Plot training history (Figure 4.1)
    print("\n[STEP 5] Generating training plots...")
    plot_training_history(history)

    print(f"\n[DONE] Model saved to: {MODEL_SAVE_PATH}")
    print("  Run the app with:  streamlit run app.py")


if __name__ == "__main__":
    main()
