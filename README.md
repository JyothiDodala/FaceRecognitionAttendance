
# Face Recognition Attendance System

This is a Face Recognition-based Attendance System built with Python. It can capture dataset images, train a model, recognize faces in real-time, and record attendance automatically.

Folder Structure:

FaceProject/

* data/                  # Captured face images
* Dataset/               # Optional pre-collected dataset images
* attendance.csv         # Attendance log
* encodings.pkl          # Saved face encodings after training
* train.py               # Model training script
* main.py                # Face recognition & attendance script
* demo.py                # Step-by-step interactive demo
* super_demo.py          # Automatic demo script
* gui.py                 # Optional GUI interface
* camera_demo.py         # Camera test script
* capture.py             # Dataset capture script
* test_camera.py         # Optional camera test
* README.md              # Project documentation
* requirements.txt       # Required Python packages

Installation:

1. Clone or download the project.
2. Open Anaconda Prompt (or terminal) in the project folder.
3. (Optional) Create or activate a Python environment:
   conda create -n faceenv python=3.10
   conda activate faceenv
4. Install required packages:
   pip install -r requirements.txt

Usage:

Automatic Demo:
Run the automatic demo script:
python super_demo.py

* Trains the model (if not already trained)
* Starts face recognition using the camera
* Updates and saves attendance automatically
  Press `q` in the camera window to stop the feed.

Step-by-Step Demo:
Run the interactive demo:
python demo.py

* Capture dataset images (`c` to capture, `q` to quit)
* Train the model
* Start recognition
* View recorded attendance

GUI Version (Optional):
Run the GUI interface:
python gui.py

* Provides buttons for Capture Dataset, Train Model, Start Camera, and Show Attendance

Notes:

* Ensure the camera is not being used by other applications.
* Keep at least 3–5 face images in `data/` for accurate recognition.
* Attendance is logged in `attendance.csv`.

Dependencies:

All required Python packages are listed in `requirements.txt`. Install them using:
pip install -r requirements.txt

Script Reference:

Script Name: train.py
What It Does: Trains the face recognition model from dataset
Key Points: Generates encodings.pkl; run once if new images are added

Script Name: main.py
What It Does: Starts camera, recognizes faces, logs attendance
Key Points: Shows live recognition; updates attendance.csv; press q to stop

Script Name: super_demo.py
What It Does: Runs the full workflow automatically
Key Points: Trains model if needed, starts recognition, logs attendance

Script Name: demo.py
What It Does: Step-by-step workflow
Key Points: Capture dataset → train → recognize → view attendance

Script Name: gui.py
What It Does: GUI interface for the project
Key Points: Buttons for Capture Dataset, Train Model, Start Camera, Show Attendance

Script Name: camera_demo.py
What It Does: Tests the camera feed
Key Points: Verifies camera functionality

Script Name: capture.py
What It Does: Capture new dataset images
Key Points: Press c to capture, q to quit; saves images in data/

Script Name: test_camera.py
What It Does: Optional camera test
Key Points: Quick camera verification
