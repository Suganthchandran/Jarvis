import pyttsx3  # Converts text to speech
import speech_recognition as sr  # Recognize speech from the user
import datetime
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import pywhatkit as wk
import os

engine = pyttsx3.init('sapi5')  # sapi5 is a TSS engine from Windows
voices = engine.getProperty('voices')  # Gets the voices installed on the system
engine.setProperty('voice', voices[0].id)  # 0 is Male Voice and 1 is Female Voice
engine.setProperty('rate', 200)  # Set the speed at which the engine speaks. 150 is a good average speed

def speak(audio):
    engine.say(audio)  # Tells the engine what text to say
    engine.runAndWait()  # Processes the speech queue and waits for the speech to complete

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # This line opens the microphone to capture the user's voice
        print('Listening...')
        r.pause_threshold = 1  # After 1 second of silence, assume the user has finished speaking
        audio = r.listen(source)  # Listen to the user's speech

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  # Converts the speech into text using Google's API
        print(f"User said: {query}\n")

    except Exception as e:
        print('Say that again please...')
        return "None"  # Returns None if the speech couldn't be recognized
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")

    print("Ready to Comply. What can I do for you Sir...")
    speak("Ready to Comply. What can I do for you Sir")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  # Convert recognized speech to lowercase for consistency

        if query == "none":  # Handle the case when recognition fails
            continue

        if 'jarvis' in query:  # Respond only if "jarvis" is mentioned
            print("Yes Sir")
            speak("Yes Sir")

        elif 'who are you' in query:
            print("My Name is Jarvis")
            speak('My Name is Jarvis')
            print("I can do Everything that my creator programmed me to do...")
            speak("I can do Everything that my creator programmed me to do...")

        elif 'who created you' in query:
            print("I am created by a genius developer whose name is Batman")
            speak("I am created by a genius developer whose name is Batman")

        elif 'what is' in query:
            speak('Searching Wikipedia')
            query = query.replace('what is','')  # Replace the 'what is' with nothing => so that when we say ('What is cosmology') , it will becomes only cosmology and search it.
            results = wikipedia.summary(query, sentences=2)  # sentences=2 means only 2 sentence will be fetched from the wikipedia
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia')
            query = query.replace('who is','')  # Replace the 'what is' with nothing => so that when we say ('What is cosmology') , it will becomes only cosmology and search it.
            results = wikipedia.summary(query, sentences=2)  # sentences=2 means only 2 sentence will be fetched from the wikipedia
            speak('According to Wikipedia')
            print(results)
            speak(results)
        
        elif 'just open youtube' in query:
            speak('Youtube is now opening')
            webbrowser.open('youtube.com')

        elif 'just open google' in query:
            speak('Google is now opening')
            webbrowser.open('google.com')

        elif 'open google' in query:  
            speak('What should I search ?')
            while True:
                search = takeCommand().lower()
                if search:
                    if 'no need to search' in search or 'no need to' in search:
                        speak('Ok Sir. Just opening Google')
                        webbrowser.open('google.com')
                        break
                    webbrowser.open(f"https://www.google.com/search?q={search}")
                    speak(f"Searching about {search}")
                    try:
                        speak('Do i have to search deeper about it, Sir...')
                        reply = takeCommand().lower()
                        if reply:
                            if 'yes' in reply or 'okay' in reply or 'ok' in reply or 'yes search it' in reply:
                                webbrowser.open(f"https://en.wikipedia.org/wiki/{search}")
                                speak('Here is your results Sir')
                                break
                            if 'no' in reply or 'not now' in reply or 'no need' in reply:
                                print('Ok Sir...')
                                speak('Ok Sir')
                                break
                            else:
                                speak("I didn't quite catch that. Please respond with yes or no.")
                        break
                    except wikipedia.exceptions.DisambiguationError as e:
                        speak("There are multiple results. Please specify.")
                        continue
                    except wikipedia.exceptions.PageError:
                        speak("I couldn't find anything on Wikipedia.")
                        break
                    except Exception as e:
                        speak(f"An error occurred: {str(e)}")
                        break

        elif 'play' in query and 'on youtube' in query:
            search = query.replace('play', '').replace('on youtube', '').strip()
            if search:
                wk.playonyt(search)  # Use pywhatkit to play the video on YouTube
                speak(f"Playing {search} on YouTube.")

        elif 'open youtube' in query:  
            speak('What would you like to watch ?')
            while True:
                search = takeCommand().lower()
                if search:
                     if 'no need to search' in search or 'no need to' in search:
                        speak('Ok Sir. Just opening Youtube')
                        webbrowser.open('youtube.com')
                        break
                     wk.playonyt(f"{search}")
                     speak('Here is your video Sir')
                     break
                
        elif 'close brave' in query:
            os.system("taskkill /f /im brave.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close edge' in query:
            os.system("taskkill /f /im msedge.exe")

        if 'open' in query:
            path = r"C:\Windows\System32\mspaint.exe"
            speak('Opening Paint')
            os.startfile(path)

        if 'exit' in query or 'stop' in query:  # Option to exit the loop
            print("Goodbye Sir")
            speak("Goodbye Sir")
            break  # Break the loop and stop the program
