from ultralytics import YOLO
import cv2

# -------------------------
# SETTINGS
# -------------------------
use_webcam = True       # True = webcam, False = video file
video_path = "sample_video.mp4"  # Video file path (ignored if webcam = True)
object_class = 0          # 0=person, 2=car, 3=motorcycle, etc.
output_file = "output.mp4"  # Save processed video here

# -------------------------
# LOAD YOLO MODEL
# -------------------------
model = YOLO("yolov8n.pt")  # 'n' = nano version (fastest)

# -------------------------
# OPEN VIDEO SOURCE
# -------------------------
if use_webcam:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# -------------------------
# SETUP VIDEO WRITER
# -------------------------
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use MJPG for better macOS compatibility
output_file = "output.avi"  # Save as AVI format
out = cv2.VideoWriter(output_file, fourcc, 20.0,
                      (int(cap.get(3)), int(cap.get(4))))


# -------------------------
# PROCESS EACH FRAME
# -------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 detection + tracking
    results = model.track(frame, persist=True, classes=[object_class])

    # Draw detections
    annotated_frame = results[0].plot()

    # Count detected objects
    num_objects = len(results[0].boxes)
    cv2.putText(annotated_frame, f"Count: {num_objects}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    # Show result
    cv2.imshow("YOLOv8 Tracking", annotated_frame)

    # Save frame to output video
    out.write(annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# -------------------------
# CLEANUP
# -------------------------
cap.release()
out.release()
cv2.destroyAllWindows()

