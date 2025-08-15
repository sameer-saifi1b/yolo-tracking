# 🎯 YOLOv8 Object Tracking

This project uses **YOLOv8** for real-time object detection and tracking in videos.  
If the object leaves and comes back into the frame, it is detected again.

---

## 📌 Features
- Real-time object detection using YOLOv8
- Object tracking across frames
- Supports MP4, AVI, and webcam streams
- Automatic re-identification if the object reappears

---

## 🛠 Requirements
- Python 3.8+
- OpenCV
- Ultralytics YOLO
- NumPy

Install dependencies:
```bash
pip install ultralytics opencv-python numpy

🚀 How to Run

Clone the repository:

git clone https://github.com/sameer-saifi1b/yolo-tracking.git
cd yolo-tracking


Place your video file in the project folder and name it:

sample_video.mp4


Run the script:

python yolo_tracking.py


Output will be saved as:

output.mp4

📂 Project Structure
yolo_tracking/
│── yolo_tracking.py   # Main Python script
│── sample_video.mp4   # Test video (not included in repo)
│── output.mp4         # Result video (ignored in .gitignore)
│── .gitignore         # Ignore unnecessary files
│── README.md          # This file

🏆 Author

Developed by SAMEER SAIFI
