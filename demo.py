import cv2
import os
import subprocess
import sys
import time

# --- Setup ---
DATASET_DIR = "data"
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# --- Step 1: Capture Dataset ---
print("Step 1: Dataset Capture")
cap = cv2.VideoCapture(0)
count = 0
if not cap.isOpened():
    print("Cannot access camera")
    sys.exit()

print("Press 'c' to capture image, 'q' to finish capturing")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Dataset Capture", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        filename = os.path.join(DATASET_DIR, f"img_{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Captured {count} images.\n")
time.sleep(1)

# --- Step 2: Train Model ---
print("Step 2: Training Model")
try:
    subprocess.run([sys.executable, "train.py"], check=True)
    print("Model trained successfully!\n")
except subprocess.CalledProcessError:
    print("Error running train.py")
    sys.exit()

time.sleep(1)

# --- Step 3: Start Recognition ---
print("Step 3: Start Recognition (Press 'q' to stop)")
try:
    subprocess.run([sys.executable, "main.py"], check=True)
except subprocess.CalledProcessError:
    print("Error running main.py")
    sys.exit()

# --- Step 4: Show Attendance ---
print("\nStep 4: Attendance")
if os.path.exists("attendance.csv"):
    with open("attendance.csv", "r") as f:
        print(f.read())
else:
    print("Attendance file not found.")

print("\nDemo complete! ✅")