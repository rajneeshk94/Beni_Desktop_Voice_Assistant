import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#Runs the Voice Assistant
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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'You said: {query}\n') 

    except Exception as e:
        print('Please speak again!')
        return 'None'
    return query                               

if __name__ == '__main__':
    wish_me()

    while True:
        query = takeCommand().lower()   

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 