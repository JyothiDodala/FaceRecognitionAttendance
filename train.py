import face_recognition
import os
import pickle

dataset_path = "dataset"

known_encodings = []
known_names = []

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        if len(face_locations) > 0:
            encoding = face_recognition.face_encodings(image, face_locations)[0]
            known_encodings.append(encoding)
            known_names.append(person_name)
            print("Encoded:", image_name)
        else:
            print("No face found:", image_name)

data = {"encodings": known_encodings, "names": known_names}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Training Completed")