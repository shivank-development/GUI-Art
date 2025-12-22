import pyttsx3

engine = pyttsx3.init()

msg = input("Enter text to speak: ")
speed = int(input("Speed (100-300): "))

engine.setProperty("rate", speed)  # Set speaking speed

engine.say(msg)
engine.runAndWait()