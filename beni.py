import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 16:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak("Hey there!, I'm Beni. How may I help you?")                

if __name__ == '__main__':
    wish_me()    