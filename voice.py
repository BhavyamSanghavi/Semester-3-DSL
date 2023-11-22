import pyttsx3 as p
import datetime 
import speech_recognition 
import wikipedia
import webbrowser
import os


engine=p.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):    speak("Good Morning Bhaavyam")
    elif(hour>=12 and hour<17): speak("Good Afternoon Bhaavyam")
    elif(hour>=17 and hour<20): speak("Good Evening Bhaavyam")
    else:   speak("Good Night Bhaavyam")

def takeCommand():
    # takes input from me and converts into string
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        speak("Listening....")
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again Please....")
        return "None"
    return query

# def sendemail(to, content):


if __name__=='__main__':
    wish()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia",results)
        
        elif "open youtube" in query:
            speak("opening You Tube")
            webbrowser.open("youtube.com")
        
        elif "open gmail" in query:
            speak("Opening Gmail Bhaavyam")
            webbrowser.open("gmail.com")
        
        elif "open code chef" in query:
            speak("opening code chef")
            webbrowser.open("codechef.com")

        elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif "open telegram" in query:
            codepath="C:\\Users\\acer\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codepath)
        
        elif "day" in query:
            strday=datetime.datetime.now().weekday()
            speak(f"Today is {strday}"+"Bhaavyam")

        elif "shut down" in query:
            speak("Shutting down Bhaavyam Bye bye")
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak("Restarting computer Bhaavyam")
            os.system("shutdown /r /t 1")
        
        elif "stop" in query:
            speak("Bye Bye Bhaavyam")
            exit()
            
