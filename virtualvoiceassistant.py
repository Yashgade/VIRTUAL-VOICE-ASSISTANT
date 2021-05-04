import shutil
import subprocess
import time
import pyjokes as pyjokes
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  !")
    else:
        speak("Good Evening !")
    speak("I am quantom .")


def usrname():
    speak("What is your name? ")
    uname = takeCommand()
    speak("Hola......" + uname)
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you?")
    return uname


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "human"
    return query


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    usrname()
    while True:
        query = takeCommand().lower()

        # ------------------------------------------------------------------------
        # ------------------------------ wikipedia--------------------------------

        if 'wikipedia' in query:
            speak('Searching ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "tell me" in query:
            app_id = "YVEU9Q-86292EX7RR"
            client = wolframalpha.Client(app_id)

            indx = query.split().index('me')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)

        # ------------------------------------------------------------------------
        # -----------------------------General Commands---------------------------

        elif 'hello' in query:
            speak("Hello Sir I am quantom")

        elif 'how are you' in query:
            speak("I am fine Thank you")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            name = query

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("quantom")

        elif "who i am" in query:
            speak("Definately Human")

        elif "why you came to world" in query:
            speak("Thanks to KKW STUDENTS. further It's a secret")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by KKW STUDENTS.")

        elif "who are you" in query:
            speak("I am your virtual assistant created by KKW STUDENTS")

        elif 'reason for you' in query:
            speak("I was created as a Mini project ")

        # ------------------------------------------------------------------------
        # --------------------------------News------------------------------------

        elif 'news' in query:
            speak('Showing news...')
            webbrowser.open("timesofindia.indiatimes.com")

        elif 'open BBC news' in query:
            speak("Opening BBC")
            webbrowser.open("https://www.bbc.com/hindi")

        elif 'open scroll' in query:
            speak("Opening news from scroll.in")
            webbrowser.open("scroll.in")

        # ------------------------------------------------------------------------
        # -------------------------------- Music ---------------------------------

        elif 'youtube music' in query:
            speak('Playing youtube music...')
            webbrowser.open("music.youtube.com/watch?v=ktvTqknDobU&list=RDCLAK5uy_lmVWEkkypRcXdChTg534p8SRNSfkhj3rA")

        elif 'youtube bollywood music' in query:
            speak('Playing bollywood youtube music...')
            webbrowser.open("music.youtube.com/watch?v=zjMtaw2mrrc&list=RDCLAK5uy_kjNBBWqyQ_Cy14B0P4xrcKgd39CRjXXKk")

        elif 'play music' in query:
            speak("Enjoy the music!!")
            music_dir = 'G:\\songsvoice'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        # ------------------------------------------------------------------------
        # -------------------------- Educational sites----------------------------

        elif 'open stack overflow' in query:
            speak('Opening stackoverflow...')
            webbrowser.open("stackoverflow.com")

        elif 'open coursera' in query:
            speak('Opening coursera...')
            webbrowser.open("coursera.org")

        elif 'open udemy' in query:
            speak('Opening udemy...')
            webbrowser.open("udemy.com")

        elif 'k k wagh college' in query:
            speak('Opening K K Wagh page...')
            webbrowser.open("engg.kkwagh.edu.in")

        elif 'open edureka' in query:
            speak("Opening edureka")
            webbrowser.open("edureka.co")

        elif 'open geeks for geeks' in query:
            speak("Opening geeks for geeks")
            webbrowser.open("geeksforgeeks")

        elif 'open w 3 schools' in query:
            speak("Opening w 3 schools")
            webbrowser.open("w3schools.com")

        # ------------------------------------------------------------------------
        # -------------------------------E-commerse-------------------------------

        elif 'open amazon' in query:
            speak('Opening amazon...')
            webbrowser.open("amazon.in")

        elif 'open flipkart' in query:
            speak('Opening flipkart...')
            webbrowser.open("flipkart.com")

        # ------------------------------------------------------------------------
        # -------------------------------- Notes----------------------------------

        elif "write a note" in query:
            speak("What should i write?")
            note = takeCommand()
            file = open('quantom.txt', 'w')
            speak("Should i include date and time")
            query = takeCommand()
            if 'yes' in query or 'sure' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("quantom.txt", "r")
            print(file.read())

        # ------------------------------------------------------------------------
        # ---------------------------- Browse Internet----------------------------

        elif 'open youtube' in query:
            speak('Opening YouTube...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening google...')
            webbrowser.open("google.com")

        elif 'search' in query:
            statement = query.replace("search", "")
            webbrowser.open_new_tab(statement)

        elif "local weather" in query:
            query = "what is the local weather"
            app_id = "YVEU9Q-86292EX7RR"
            client = wolframalpha.Client(app_id)

            indx = query.split().index('is')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer1 = next(res.results).text
            speak(answer1)

        # --------------------------------------------------------------------------
        # ------------------------------ Visual Studio------------------------------

        elif 'open code' in query:
            speak("processing...")
            codePath = "F:\\VisualStudioCode\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # -------------------------------------------------------------------------
        # ---------------------------------- Time----------------------------------

        elif 'tell  time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        # -------------------------------------------------------------------------
        # --------------------------------- Funny----------------------------------

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # --------------------------------------------------------------------------
        # ------------------------------- System Command----------------------------

        elif 'shutdown system' in query or 'log off system' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Have a nice day !")
            elif hour >= 12 and hour < 18:
                speak("Have a nice day  !")
            else:
                speak("good night !")
                os.system("shutdown /s /t 1")

        # --------------------------------------------------------------------------
        # ------------------------------- Turn Off Assistance-----------------------

        elif "ok bye" in query:
            speak('your personal assistant quantom is shutting down,Good bye')
            print('your personal assistant quantom is shutting down,Good bye')
            break

