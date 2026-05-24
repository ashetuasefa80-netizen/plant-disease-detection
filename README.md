# 🌿 Plant Disease Detection System

**Madda Walabu University — College of Computing**  
**Department of Computer Science**  
**Course:** Artificial Intelligence Project  
**Author:** Morketa Negash (Ugrr/51983/15)  
**Instructor:** Shume. B  

---

## 📋 Project Overview

An end-to-end AI system that detects plant diseases from leaf images using a
**Convolutional Neural Network (CNN)** trained on 16,000 images from the
PlantVillage dataset. The model is deployed via a **Streamlit** web interface
that provides instant diagnosis, confidence scores, and treatment recommendations.

**Supported Crops:** Apple · Corn · Potato · Tomato  
**Total Disease Classes:** 21 (including healthy classes)

---

## 🗂️ Project Structure

```
Plant disease detection system/
│
├── app.py                        ← Main Streamlit web application
├── requirements.txt              ← Python dependencies
├── setup.bat                     ← One-click setup script (Windows)
├── run_app.bat                   ← Launch the web app
├── run_training.bat              ← Start model training
│
├── model/
│   ├── train_model.py            ← CNN training script (Chapter 4.4)
│   ├── predictor.py              ← Inference / prediction module
│   ├── disease_info.py           ← Disease database + treatment advice
│   ├── plant_disease_cnn.h5      ← Saved model (created after training)
│   └── class_names.json          ← Class index map (created after training)
│
├── utils/
│   ├── download_dataset.py       ← Kaggle dataset downloader
│   ├── evaluate_model.py         ← Metrics + confusion matrix (Table 4.1)
│   └── demo_mode.py              ← Simulated predictions for UI testing
│
└── dataset/                      ← PlantVillage images (you add this)
    ├── Apple___Apple_scab/
    ├── Apple___healthy/
    ├── Tomato___Late_blight/
    └── ...
```

---

## 🚀 Quick Start (Windows)

### Step 1 — Install & Setup
Double-click **`setup.bat`** or run in CMD:
```cmd
setup.bat
```
This creates a virtual environment and installs all dependencies.

---

### Step 2 — Get the Dataset

**Option A — Kaggle (Automatic):**
```cmd
pip install kaggle
python utils/download_dataset.py
```
You need a Kaggle account and `kaggle.json` in `~/.kaggle/`.

**Option B — Manual Download:**
1. Go to: https://www.kaggle.com/datasets/emmarex/plantdisease
2. Download and extract the ZIP
3. Place the class folders inside the `dataset/` folder:
   ```
   dataset/
   ├── Apple___Apple_scab/   ← .jpg images here
   ├── Apple___healthy/
   └── ...
   ```

**Verify your dataset:**
```cmd
python utils/download_dataset.py --verify
```

---

### Step 3 — Train the CNN Model
Double-click **`run_training.bat`** or run:
```cmd
python model/train_model.py
```
- Training runs for **30 epochs** with early stopping
- Best model saved to `model/plant_disease_cnn.h5`
- Training plots saved to `model/training_history.png`
- Expected accuracy: **~94.5%** (Table 4.1)

---

### Step 4 — Run the Web Application
Double-click **`run_app.bat`** or run:
```cmd
streamlit run app.py
```
Open your browser at: **http://localhost:8501**

---

## 🧪 Demo Mode (No Training Required)

If you haven't trained the model yet, the app runs in **Demo Mode**
automatically. You can upload any leaf image and see the full UI with
simulated predictions — useful for testing the interface.

---

## 📊 Model Performance (Table 4.1)

| Metric    | Value  |
|-----------|--------|
| Accuracy  | 94.5%  |
| Precision | 92.0%  |
| Recall    | 91.5%  |
| F1-Score  | 91.7%  |

---

## ⚙️ CNN Architecture (Chapter 4.4)

```
Input (224×224×3)
    ↓
Conv Block 1: Conv2D(32) → BN → Conv2D(32) → BN → MaxPool → Dropout
    ↓
Conv Block 2: Conv2D(64) → BN → Conv2D(64) → BN → MaxPool → Dropout
    ↓
Conv Block 3: Conv2D(128) → BN → Conv2D(128) → BN → MaxPool → Dropout
    ↓
Conv Block 4: Conv2D(256) → BN → Conv2D(256) → BN → MaxPool → Dropout
    ↓
Conv Block 5: Conv2D(512) → BN → MaxPool → Dropout
    ↓
Flatten → Dense(512) → BN → Dropout → Dense(256) → Dropout
    ↓
Softmax Output (21 classes)
```

**Optimizer:** SGD with Momentum (SGDM), lr=0.001, momentum=0.9  
**Loss:** Categorical Cross-Entropy

---

## 🔬 Evaluate the Trained Model

After training, generate the full metrics report and confusion matrix:
```cmd
python utils/evaluate_model.py
```

---

## 📦 Dependencies

| Package         | Version  | Purpose                        |
|-----------------|----------|--------------------------------|
| tensorflow      | 2.13.0   | CNN model training & inference |
| streamlit       | 1.28.0   | Web interface                  |
| numpy           | 1.24.3   | Numerical operations           |
| Pillow          | 10.0.1   | Image loading & preprocessing  |
| opencv-python   | 4.8.1.78 | Image processing               |
| scikit-learn    | 1.3.0    | Evaluation metrics             |
| plotly          | 5.17.0   | Interactive charts             |
| matplotlib      | 3.7.2    | Training plots                 |

---

## 🌱 Future Work (Chapter 5.4)

- Expand to Ethiopian staple crops: Teff, Wheat, Barley
- Mobile app deployment (Android/iOS)
- IoT / drone integration for real-time field monitoring
- Automated retraining loop with expert verification

---

*Madda Walabu University · Bale Robe, Ethiopia · May 2026*
