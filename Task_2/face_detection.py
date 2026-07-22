import cv2


# Load OpenCV's pretrained face-detection model
model_path = (
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)

face_detector = cv2.CascadeClassifier(model_path)

if face_detector.empty():
    print("Face detection model could not be loaded.")
    exit()


# CAP_DSHOW often fixes webcam issues on Windows
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Camera could not be opened.")
    print("Close Camera, Zoom, Meet, Teams or other camera applications.")
    print("You may also try changing camera index 0 to 1.")
    exit()


print("=" * 45)
print("       CODSOFT FACE DETECTION")
print("=" * 45)
print("Press Q to close the program.")


while True:
    success, frame = camera.read()

    if not success or frame is None:
        print("Unable to receive a frame from the camera.")
        break

    # Mirror the camera view
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces
    detected_faces = face_detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    # Draw a box around every detected face
    for x, y, width, height in detected_faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            3
        )

        cv2.putText(
            frame,
            "Face Detected",
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Total Faces: {len(detected_faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("CodSoft Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()

print("Face detection program closed.")