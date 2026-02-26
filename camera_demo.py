import cv2
import os

DATASET_DIR = "data"
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

cap = cv2.VideoCapture(0)
count = 0

if not cap.isOpened():
    print("Cannot access camera")
    exit()

print("Press 'c' to capture image, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Face Recognition Attendance", frame)

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