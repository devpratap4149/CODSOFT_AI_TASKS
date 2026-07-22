import random
from datetime import datetime

import pyttsx3
import speech_recognition as sr


recognizer = sr.Recognizer()


def speak(text):
    """Print and speak the chatbot response."""
    print("Bot:", text)

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as error:
        print("Audio error:", error)


def listen():
    """Listen through the microphone and convert speech to text."""
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now.")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        print("Recognizing...")

        user_text = recognizer.recognize_google(audio)

        print("You:", user_text)

        return user_text.lower().strip()

    except sr.WaitTimeoutError:
        print("No voice detected.")
        speak("I did not hear anything.")
        return ""

    except sr.UnknownValueError:
        print("Voice detected, but not understood.")
        speak("Sorry, I could not understand your voice.")
        return ""

    except sr.RequestError as error:
        print("Speech recognition error:", error)
        speak(
            "The speech recognition service is unavailable. "
            "Please check your internet connection."
        )
        return ""

    except OSError as error:
        print("Microphone error:", error)
        speak(
            "The microphone was not found, "
            "or microphone permission is disabled."
        )
        return ""

    except Exception as error:
        print("Unexpected listening error:", error)
        return ""


def get_response(user_message):
    """Return a response based on predefined rules."""
    message = user_message.lower().strip()

    greetings = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if message in greetings:
        responses = [
            "Hello! How can I help you?",
            "Hi! Nice to meet you.",
            "Hey! What would you like to know?"
        ]

        return random.choice(responses)

    elif "your name" in message or "who are you" in message:
        return (
            "I am CodSoft AI Assistant, "
            "a rule-based voice chatbot."
        )

    elif "how are you" in message:
        return "I am doing great. Thank you for asking."

    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in message or "day" in message:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif "python" in message:
        return (
            "Python is a beginner-friendly programming language "
            "widely used in artificial intelligence and machine learning."
        )

    elif "machine learning" in message:
        return (
            "Machine learning allows computers "
            "to learn patterns from data."
        )

    elif "artificial intelligence" in message or message == "ai":
        return (
            "Artificial intelligence enables machines "
            "to perform tasks that normally require human intelligence."
        )

    elif "codsoft" in message:
        return (
            "CodSoft provides virtual internships "
            "and project-based learning opportunities."
        )

    elif "internship" in message:
        return (
            "For the CodSoft artificial intelligence internship, "
            "you need to complete at least three tasks."
        )

    elif "help" in message:
        return (
            "You can ask me about Python, artificial intelligence, "
            "machine learning, CodSoft, internship, date, time, "
            "or my name."
        )

    elif message in ["bye", "exit", "quit", "stop"]:
        return "Goodbye! Have a great day."

    else:
        return (
            "Sorry, I did not understand that question. "
            "Say help to know what you can ask."
        )


print("=" * 45)
print("        CODSOFT VOICE CHATBOT")
print("=" * 45)

speak("Hello Dev. I am ready to talk with you.")

while True:
    user_input = listen()

    if user_input == "":
        continue

    bot_response = get_response(user_input)

    speak(bot_response)

    if user_input in ["bye", "exit", "quit", "stop"]:
        break