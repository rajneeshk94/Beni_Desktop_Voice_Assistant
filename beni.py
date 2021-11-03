import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit

webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#Runs the Voice Assistant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def wish_me():
    # hour = int(datetime.datetime.now().hour)
    # if hour >= 0 and hour < 12:
    #     speak('Good Morning!')

    # elif hour >= 12 and hour < 16:
    #     speak('Good Afternoon!')

    # else:
    #     speak('Good Evening!')

    # speak("Hey there!, I'm Beni. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..\n')
        # r.pause_threshold = 0.5
        # r.adjust_for_ambient_noise(source, duration = 0.5)
        audio = r.listen(source)

    try:
        # print('Recognizing')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'You said: {query}\n') 

    except Exception as e:
        print('Please speak again!')
        return 'None'
    return query                               

if __name__ == '__main__':
    # wish_me()
    speak("Hey there!, I'm Beni. How may I help you?")

    while True:
        query = takeCommand().lower()   

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
             webbrowser.get('chrome').open('youtube.com')

        elif 'open google' in query:
             webbrowser.get('chrome').open('google.com')

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'Sir, the time is {time}')

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'search' in query:
            search_item = query.replace('search', '')
            speak(f'Searching {search_item} on Google')
            pywhatkit.search(search_item)
            # pywhatkit.text_to_handwriting("I'm just testing if this could really do what I wish to obtain from this module. So ya this is cool!", "C:/Users/user/Desktop/test23.png")

        elif 'goodbye' in query:
            speak('Goodbye Sir')
            break