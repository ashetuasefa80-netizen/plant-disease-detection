"""
Model Evaluation Script
Generates the performance metrics from Table 4.1 of the project report.
Produces: Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

MODEL_PATH   = "model/plant_disease_cnn.h5"
DATASET_DIR  = "dataset"
IMG_SIZE     = (224, 224)
BATCH_SIZE   = 32


def evaluate():
    # Load model
    if not os.path.exists(MODEL_PATH):
        print(f"[ERROR] Model not found at '{MODEL_PATH}'. Train first.")
        return

    print("[INFO] Loading model...")
    model = tf.keras.models.load_model(MODEL_PATH)

    # Load class names
    with open("model/class_names.json") as f:
        class_names = {int(k): v for k, v in json.load(f).items()}

    # Build test generator (no augmentation, just normalization)
    test_datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
    test_gen = test_datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False,
    )

    print(f"[INFO] Evaluating on {test_gen.samples} validation images...")

    # Predictions
    y_pred_probs = model.predict(test_gen, verbose=1)
    y_pred = np.argmax(y_pred_probs, axis=1)
    y_true = test_gen.classes

    # ── Metrics (Table 4.1) ──────────────────────────────────────────
    acc  = accuracy_score(y_true, y_pred) * 100
    prec = precision_score(y_true, y_pred, average="weighted", zero_division=0) * 100
    rec  = recall_score(y_true, y_pred, average="weighted", zero_division=0) * 100
    f1   = f1_score(y_true, y_pred, average="weighted", zero_division=0) * 100

    print("\n" + "=" * 50)
    print("  EXPERIMENTAL RESULTS (Table 4.1)")
    print("=" * 50)
    print(f"  Accuracy  : {acc:.2f}%")
    print(f"  Precision : {prec:.2f}%")
    print(f"  Recall    : {rec:.2f}%")
    print(f"  F1-Score  : {f1:.2f}%")
    print("=" * 50)

    # Per-class report
    class_labels = [class_names[i] for i in sorted(class_names.keys())]
    print("\nPer-Class Classification Report:")
    print(classification_report(y_true, y_pred, target_names=class_labels, zero_division=0))

    # ── Confusion Matrix ─────────────────────────────────────────────
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(16, 14))
    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Greens)
    plt.colorbar(im, ax=ax)

    tick_marks = np.arange(len(class_labels))
    short_labels = [c.replace("___", "\n").replace("_", " ") for c in class_labels]
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xticklabels(short_labels, rotation=45, ha="right", fontsize=7)
    ax.set_yticklabels(short_labels, fontsize=7)

    ax.set_title("Confusion Matrix — Plant Disease CNN", fontsize=14, pad=15)
    ax.set_xlabel("Predicted Label", fontsize=11)
    ax.set_ylabel("True Label", fontsize=11)

    # Annotate cells
    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            if cm[i, j] > 0:
                ax.text(j, i, str(cm[i, j]),
                        ha="center", va="center", fontsize=6,
                        color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    save_path = "model/confusion_matrix.png"
    plt.savefig(save_path, dpi=150)
    print(f"\n[INFO] Confusion matrix saved to: {save_path}")
    plt.show()


if __name__ == "__main__":
    evaluate()
