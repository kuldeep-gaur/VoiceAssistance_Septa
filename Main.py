import speech_recognition as sr
import pyttsx3
import webbrowser
import MusicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def ProcessCommand(c):
    print(c)
    if("open google" in c.lower()):
        webbrowser.open("https://www.google.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com")
    elif("open facebook" in c.lower()): 
        webbrowser.open("https://www.facebook.com")
    elif("open twitter" in c.lower()):
        webbrowser.open("https://twitter.com")
    elif("open instagram" in c.lower()): 
        webbrowser.open("https://www.instagram.com")
    elif(c.lower().startswith("play")):
 # Extract the song name from the command
        song = c.lower().split(" ")[1]
        print(song)
        link = MusicLibrary.music[song]
        webbrowser.open(link)
 
if __name__ == "__main__":
    speak("Initializing voice assistant... septa")
    while True:

 # Listen for the Activate word my Voice Assistant
        r= sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for the activation word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
 
            word = r.recognize_google(audio)
 
            if ("septa" in word.lower()):
                print("Septa is activated")
                speak("Yes, how can I help you?")
                # Listen for the command after activation word
 
                with sr.Microphone() as source:
                    print("Septa is active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    print("Command received: " + command)
                    ProcessCommand(command) # Call your command processing function here
 
 
        except sr.WaitTimeoutError:
            print("Listening for you command....") 

 # print("Recognizing...")
 # hashtag#recognize speech using sphinx
 # try:
 # command = r.recognize_google(audio)
 # print("sphinx thinks you said: " + command)
 # except sr.UnknownValueError:
 # print("Sphinx could not understand audio")
 # except sr.RequestError as e:
 # print("Sphinx error; {0}".format(e))