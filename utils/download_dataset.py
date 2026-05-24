"""
Dataset Download Helper
Downloads and organizes the PlantVillage dataset from Kaggle.
The dataset contains 16,000+ leaf images across multiple crop species.
"""

import os
import sys
import zipfile
import shutil


def check_kaggle():
    """Check if Kaggle API is configured."""
    kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_json):
        print("\n[ERROR] Kaggle API credentials not found.")
        print("\nTo set up Kaggle API:")
        print("  1. Go to https://www.kaggle.com/account")
        print("  2. Click 'Create New API Token'")
        print("  3. Place the downloaded kaggle.json in: ~/.kaggle/kaggle.json")
        print("  4. Run: pip install kaggle")
        return False
    return True


def download_plantvillage(output_dir="dataset"):
    """Download PlantVillage dataset using Kaggle API."""
    if not check_kaggle():
        print("\n[ALTERNATIVE] Manual download:")
        print("  1. Visit: https://www.kaggle.com/datasets/emmarex/plantdisease")
        print("  2. Download and extract to the 'dataset/' folder")
        print("  3. Ensure structure: dataset/ClassName/image.jpg")
        return

    try:
        import kaggle
    except ImportError:
        print("[ERROR] Kaggle package not installed. Run: pip install kaggle")
        return

    print("[INFO] Downloading PlantVillage dataset from Kaggle...")
    os.makedirs(output_dir, exist_ok=True)

    kaggle.api.dataset_download_files(
        "emmarex/plantdisease",
        path=output_dir,
        unzip=True
    )
    print(f"[DONE] Dataset downloaded to: {output_dir}/")


def verify_dataset(dataset_dir="dataset"):
    """Verify the dataset structure and count images."""
    if not os.path.exists(dataset_dir):
        print(f"[ERROR] Dataset directory '{dataset_dir}' not found.")
        return False

    classes = [d for d in os.listdir(dataset_dir)
               if os.path.isdir(os.path.join(dataset_dir, d))]

    if not classes:
        print(f"[ERROR] No class folders found in '{dataset_dir}'.")
        return False

    total_images = 0
    print(f"\n[INFO] Dataset verification — {len(classes)} classes found:\n")
    print(f"  {'Class Name':<45} {'Images':>8}")
    print("  " + "-" * 55)

    for cls in sorted(classes):
        cls_path = os.path.join(dataset_dir, cls)
        images = [f for f in os.listdir(cls_path)
                  if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        total_images += len(images)
        print(f"  {cls:<45} {len(images):>8}")

    print("  " + "-" * 55)
    print(f"  {'TOTAL':<45} {total_images:>8}\n")
    print(f"[OK] Dataset is ready for training.")
    return True


if __name__ == "__main__":
    if "--verify" in sys.argv:
        verify_dataset()
    else:
        download_plantvillage()
        verify_dataset()
