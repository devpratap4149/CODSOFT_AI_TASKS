# Task 1: Rule-Based Voice Chatbot

This project was developed as part of the **CodSoft Artificial Intelligence Internship**.

## Project Overview

This is a rule-based voice chatbot built using Python.

The chatbot listens to the user through the microphone, converts speech into text, checks the message using predefined rules, and gives both text and voice responses.

## Features

- Accepts voice input through the microphone
- Converts speech into text
- Gives voice and text responses
- Responds to greetings
- Answers basic questions about Python and Artificial Intelligence
- Shows the current date and time
- Handles unknown questions
- Supports commands such as `bye`, `exit`, `quit`, and `stop`

## Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Random module
- Datetime module

## Installation

Install the required libraries using:

```bash
python -m pip install pyttsx3 SpeechRecognition PyAudio
```

## How to Run

Open the terminal inside the project folder and run:

```bash
python chatbot.py
```

After the chatbot starts, speak clearly into the microphone.

Example:

```text
Bot: Hello Dev. I am ready to talk with you.

Listening... Speak now.

You: What is Python?

Bot: Python is a beginner-friendly programming language widely used in artificial intelligence and machine learning.
```

Say `bye`, `exit`, `quit`, or `stop` to close the chatbot.

## How It Works

The chatbot uses the `SpeechRecognition` library to capture the user's voice and convert it into text.

The converted text is checked using predefined conditions and pattern matching.

The chatbot then selects an appropriate response.

The `pyttsx3` library converts the chatbot's response into speech.

## Project Structure

```text
TASK_1_CHATBOT
│
├── chatbot.py
├── README.md
└── screenshot.png
```

## Output

The program displays:

- The user's recognized speech
- The chatbot's text response
- The chatbot's spoken response
- Listening and recognition status



## Learning Outcomes

- Learned how to build a rule-based chatbot
- Learned how to use conditional statements for conversation flow
- Learned how speech recognition works
- Learned how to convert text into speech
- Learned how to work with microphone input
- Learned how to handle errors in voice recognition

## Future Improvements

- Add more questions and responses
- Add a graphical user interface
- Add support for multiple languages
- Store conversation history
- Connect the chatbot with an AI API
- Add weather and news responses

## Author

**Dev Pratap Singh**