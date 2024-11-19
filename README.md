# Face Tracker

This project is a simple face tracking application using OpenCV in Python. It captures video from the default camera, detects faces in real-time, and draws rectangles around them.

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Install OpenCV using pip:
  ```bash
  pip install opencv-python
  ```

## Usage

1. Clone the repository:
  ```bash
  git clone https://github.com/iamtomshaw/python-opencv-face-tracker.git
  cd python-opencv-face-tracker
  ```

2. Run the script:
  ```bash
  python main.py
  ```

## Code Explanation

```python
import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Access the default camera (index 0)
cap = cv2.VideoCapture(0)

# Check if the camera is opened correctly
if not cap.isOpened():
  print("Error: Could not access the camera")
  exit()

while True:
  # Capture frame-by-frame from the camera
  ret, frame = cap.read()
  
  # If frame was not captured correctly, skip this iteration
  if not ret:
    print("Error: Couldn't retrieve frame")
    continue

  # Convert the frame to grayscale for face detection and detect faces
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(300, 300))

  # Draw a rectangle around each detected face
  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

  # Display the resulting frame with detected faces
  cv2.imshow('Face Detection', frame)

  # Break the loop if the user presses the 'q' key
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```

- **Loading the Haar Cascade Classifier**: The script uses a pre-trained Haar Cascade classifier for face detection.
- **Accessing the Camera**: It accesses the default camera (index 0) for video capture.
- **Frame Capture**: Captures frames from the camera in a loop.
- **Face Detection**: Converts each frame to grayscale and detects faces using the classifier.
- **Drawing Rectangles**: Draws rectangles around detected faces.
- **Displaying Frames**: Displays the frames with detected faces in a window.
- **Exiting**: The loop breaks and the program exits when the 'q' key is pressed.

## License

This project is licensed under the MIT License.