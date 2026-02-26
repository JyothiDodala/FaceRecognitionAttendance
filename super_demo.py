import os
import subprocess
import sys
import time

# --- Paths ---
DATASET_DIR = "data"
if not os.path.exists(DATASET_DIR):
    print("Dataset folder not found. Please capture some images first!")
    sys.exit()

# --- Step 1: Train Model ---
print("Step 1: Training Model...")
try:
    subprocess.run([sys.executable, "train.py"], check=True)
    print("✅ Model trained successfully!\n")
except subprocess.CalledProcessError:
    print("❌ Error running train.py")
    sys.exit()

time.sleep(1)

# --- Step 2: Start Recognition ---
print("Step 2: Starting Recognition (Press 'q' in recognition window to stop)...")
try:
    subprocess.run([sys.executable, "main.py"], check=True)
except subprocess.CalledProcessError:
    print("❌ Error running main.py")
    sys.exit()

time.sleep(1)

# --- Step 3: Show Attendance ---
print("\nStep 3: Attendance")
if os.path.exists("attendance.csv"):
    with open("attendance.csv", "r") as f:
        print(f.read())
else:
    print("Attendance file not found.")

print("\n🎉 Demo complete! Ready for placement! 🎉")