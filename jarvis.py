import pyttsx3  # Converts text to speech
import speech_recognition as sr  # Recognize speech from the user

engine = pyttsx3.init('sapi5')  # sapi5 is a TSS engine from Windows
voices = engine.getProperty('voices')  # Gets the voices installed on the system
engine.setProperty('voice', voices[0].id)  # 0 is Male Voice and 1 is Female Voice
engine.setProperty('rate', 150)  # Set the speed at which the engine speaks. 150 is a good average speed

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

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()  # Convert recognized speech to lowercase for consistency

        if query == "none":  # Handle the case when recognition fails
            continue

        if 'jarvis' in query:  # Respond only if "jarvis" is mentioned
            print("Yes Sir")
            speak("Yes Sir")

        if 'exit' in query or 'stop' in query:  # Option to exit the loop
            print("Goodbye Sir")
            speak("Goodbye Sir")
            break  # Break the loop and stop the program
