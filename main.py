import face_recognition
import cv2
import pickle
import pandas as pd
from datetime import datetime

data = pickle.load(open("encodings.pkl", "rb"))
known_encodings = data["encodings"]
known_names = data["names"]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):

        matches = face_recognition.compare_faces(
            known_encodings, face_encoding, tolerance=0.5
        )

        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            df = pd.DataFrame([[name, date, time]])
            df.to_csv("attendance.csv", mode="a", header=False, index=False)

        top, right, bottom, left = face_location

        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()