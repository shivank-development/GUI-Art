import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def listen_and_act():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"You said: {command}")

            # Act based on the command
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "your name" in command:
                speak("I am your voice assistant.")
            elif "time" in command:
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")
            elif "stop" in command or "exit" in command:
                speak("Goodbye!")
                exit()
            else:
                speak("Sorry, I did not understand that.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

if __name__ == "__main__":
    while True:
        listen_and_act()
