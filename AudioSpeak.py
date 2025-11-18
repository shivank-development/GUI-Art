import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

for voice in voices:
    if "Zira" in voice.name or voice.gender == "VoiceGenderFemale":
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wiseMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")    
    else:
        speak("Good Evening")   
    speak("Lavi")
"""def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizig...")
        query=r.recognize_google(audio, Language="en-in")
        print("User said:",  query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query"""
if __name__=="__main__":
    wiseMe()
    #takecommand()
