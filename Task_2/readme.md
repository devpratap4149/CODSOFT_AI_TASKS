# Task 2: Face Detection Using OpenCV

This project was developed as part of the **CodSoft Artificial Intelligence Internship**.

## Project Overview

This Python application detects human faces in real time using a laptop webcam.

It uses OpenCV and a pretrained Haar Cascade classifier. When a face is detected, the program draws a rectangle around it and shows the total number of detected faces.

## Features

- Real-time face detection
- Webcam-based video processing
- Rectangle around detected faces
- Displays total face count
- Mirror-style camera view
- Close using `Q`, `q`, or `Esc`

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier

## Installation

Install OpenCV using:

```bash
python -m pip install opencv-python


## How to Run

Open the terminal inside the project folder and run:
            
                                    python face_detection.py


Click on the camera window and press Q, q, or Esc to close the program.

## Project Structure

TASK_5_FACE_DETECTION
│
├── face_detection.py
├── README.md
└── screenshot.png


How It Works :-
        The program loads OpenCV's pretrained Haar Cascade model.
            1. It opens the laptop webcam.
            2. It continuously captures video frames.
            3. Every frame is converted into grayscale.
            4. Faces are detected from the grayscale frame.
            5. A rectangle is drawn around each detected face.
            6. The total number of detected faces is displayed.



Output :- 
    The program displays:
        -> Live webcam video
        -> A green rectangle around every detected face
        -> Face detection text
        -> Total number of visible faces



## Learning Outcomes

- Learned how to access the webcam using OpenCV
- Understood real-time video frame processing
- Learned how Haar Cascade detects faces
- Learned how to draw rectangles and text on video frames


## Future Improvements

- Add face recognition with names
- Save detected faces
- Add attendance functionality
- Use a deep-learning face detector


Author :-  Dev Pratap Singh