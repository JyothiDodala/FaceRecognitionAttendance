import tkinter as tk
from tkinter import messagebox, scrolledtext
import cv2
from PIL import Image, ImageTk
import os
import subprocess
import sys
import threading

# --- Globals ---
cap = None
count = 0
DATASET_DIR = "data"

if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# --- Helper Functions ---
def run_script(script_name, log_widget, success_msg):
    """Run train.py or main.py in a separate thread"""
    def task():
        try:
            log_widget.insert(tk.END, f"Running {script_name}...\n")
            log_widget.see(tk.END)
            subprocess.run([sys.executable, script_name], check=True)
            log_widget.insert(tk.END, f"{success_msg}\n\n")
            log_widget.see(tk.END)
            messagebox.showinfo("Success", success_msg)
        except subprocess.CalledProcessError:
            log_widget.insert(tk.END, f"Error running {script_name}\n\n")
            log_widget.see(tk.END)
            messagebox.showerror("Error", f"Failed to run {script_name}")
    threading.Thread(target=task).start()

def show_attendance():
    """Display attendance from CSV in the log"""
    if os.path.exists("attendance.csv"):
        with open("attendance.csv", "r") as f:
            log_text.insert(tk.END, f"\n--- Current Attendance ---\n{f.read()}\n")
            log_text.see(tk.END)
    else:
        log_text.insert(tk.END, "\nAttendance file not found.\n")
        log_text.see(tk.END)

# --- Camera Functions ---
def capture_dataset_preview():
    """Start live camera feed"""
    global cap
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot access webcam")
        return

    def show_frame():
        if cap:
            ret, frame = cap.read()
            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk  # keep reference
                video_label.configure(image=imgtk)
            video_label.after(10, show_frame)

    show_frame()

def save_frame():
    """Capture current frame and save image"""
    global cap, count
    if cap:
        ret, frame = cap.read()
        if ret:
            filename = os.path.join(DATASET_DIR, f"img_{count}.jpg")
            cv2.imwrite(filename, frame)
            count += 1
            log_text.insert(tk.END, f"Saved {filename}\n")
            log_text.see(tk.END)
        else:
            messagebox.showwarning("Warning", "Failed to capture image")
    else:
        messagebox.showwarning("Warning", "Camera not started")

def exit_app():
    """Release camera and exit"""
    global cap
    if cap:
        cap.release()
    root.destroy()

# --- GUI Setup ---
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("700x650")
root.configure(bg="#f0f0f0")

# Heading
heading = tk.Label(root, text="Face Recognition Attendance", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
heading.pack(pady=10)

# Video feed label
video_label = tk.Label(root, bg="black", width=640, height=360)
video_label.pack(pady=10)

# Capture button for images
btn_snap = tk.Button(root, text="Capture Image", width=20, height=2, bg="#4CAF50", fg="white", command=save_frame)
btn_snap.pack(pady=5)

# Buttons frame
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

btn_capture = tk.Button(frame_buttons, text="📸 Start Camera Feed", width=20, height=2, bg="#4CAF50", fg="white",
                        command=capture_dataset_preview)
btn_capture.grid(row=0, column=0, padx=10, pady=5)

btn_train = tk.Button(frame_buttons, text="⚙️ Train Model", width=20, height=2, bg="#2196F3", fg="white",
                      command=lambda: run_script("train.py", log_text, "Model trained successfully!"))
btn_train.grid(row=0, column=1, padx=10, pady=5)

btn_start = tk.Button(frame_buttons, text="🎥 Start Recognition", width=20, height=2, bg="#FF9800", fg="white",
                      command=lambda: run_script("main.py", log_text, "Camera started!"))
btn_start.grid(row=1, column=0, padx=10, pady=5)

btn_attendance = tk.Button(frame_buttons, text="📄 Show Attendance", width=20, height=2, bg="#9C27B0", fg="white",
                           command=show_attendance)
btn_attendance.grid(row=1, column=1, padx=10, pady=5)

btn_exit = tk.Button(frame_buttons, text="❌ Exit", width=20, height=2, bg="#f44336", fg="white", command=exit_app)
btn_exit.grid(row=2, column=0, columnspan=2, pady=10)

# Log output
log_label = tk.Label(root, text="Status Log:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
log_label.pack()
log_text = scrolledtext.ScrolledText(root, width=80, height=12, state='normal')
log_text.pack(pady=5)

root.mainloop()