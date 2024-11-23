import cv2

def main():
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Access the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened correctly
    if not cap.isOpened():
        print("Error: Could not access the camera")
        return

    try:
        while True:
            # Capture frame-by-frame from the camera
            ret, frame = cap.read()
            
            # If frame was not captured correctly, skip this iteration
            if not ret:
                print("Error: Couldn't retrieve frame")
                continue

            # Invert the frame horizontally
            frame = cv2.flip(frame, 1)

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw a rectangle around each detected face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the resulting frame with detected faces
            cv2.imshow('Face Detection', frame)

            # Break the loop if the user presses the 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
