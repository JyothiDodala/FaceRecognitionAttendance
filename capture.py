import cv2
import os

name = input("Enter your name: ")
folder_path = f"dataset/{name}"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    cv2.imshow("Capture Dataset", frame)

    # Save every frame
    cv2.imwrite(f"{folder_path}/img{count}.jpg", frame)
    count += 1

    # Stop at 20 images
    if count >= 20:
        break

    if cv2.waitKey(1) == 27:  # Press ESC to stop early
        break

cap.release()
cv2.destroyAllWindows()
print(f"Dataset capture complete for {name}")