import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from email.message import EmailMessage
from pytube import YouTube

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant, How can I help you?")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print("You Said : ", query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query

def download():
    SAVE_PATH="E:/"
    link="https://www.youtube.com/watch?v=_QwMVSg89mo"
    yt=YouTube(link)

    try:
        yt=YouTube(link)

    except:
        print("Connection Error")

    print(yt.title)
    st=yt.streams.first()

    try:
        st.download(SAVE_PATH)

    except:
        print("Some Error Found")

if __name__=="__main__":
    wishMe()
    while True:
        query=takecommand().lower()
        if "wikipedia" in query:
            print("Searching Wikipedia...")
            speak("Searching wikipedia")
            query=query.replace("Wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("www.youtube.com")

        elif "play music" in query:
            music_dir="F:\Best Songs 6"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strftime}")
            speak(f"The time is {strftime}")

        elif "open word file" in query:
            text = "E:\jarvis chat bot.docx"
            os.startfile(text)


        elif "email" in query:
            sender = 'skshrey11@gmail.com'
            receivers = ['shrey.18bci1002@abes.ac.in']

            message = f"""\
            Subject: Hi Mailtrap
            
            This is my first message with Python."""
            
            try:
                server = smtplib.SMTP('localhost')
                server.sendmail(sender, receivers, message)
                print("Successfully sent email")

            except Exception:
                print("Error: unable to send email")

        elif "download youtube video" in query:
            speak("downloading youtube video")
            download()
            print("Task Completed !!")
            speak("Task Completed !!")
            
        elif "exit" in query:
            break

    speak("Thanks for Using, Have a nice day !!")



        
