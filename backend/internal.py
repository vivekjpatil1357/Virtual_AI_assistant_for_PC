import os
import webbrowser
import datetime
import openai
import pythoncom


# from playsound import playsound
import speech_recognition as sr
import win32com.client
import pyautogui as p
from plyer import notification
from config import apikey
import time
import external as E
import AppOpener as a
from app import app
# from main import say
def say(text):
    pythoncom.CoInitialize()    
    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Uninitialize COM when done
        pythoncom.CoUninitialize()


def chat(query):
    # print(chatStr)
    openai.api_key = apikey
    chatStr += f"Vivek: {query}\n computer:"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        say(response["choices"][0]["text"])
    except:
        say("sorry? say that again")


def isExit(query):  # if exit terminate exe.
    if "exit" in query.lower():
        say("exiting sir.....")
        exit()


def timer(t):
    say(f"timer for {t} seconds is ready for you sir")
    for i in range(t, 0, -1):
        print(i)
        time.sleep(1)
    notification.notify(
        title="Time Over", message=f"Timer for {t} seconds is over!!", timeout=3
    )
    # waiting time
    return ("Time over sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(query)
            return query
        except Exception as e:
            say("sorry ,i can't listen properly, can you say that again?")
            query = takecommand()
            return query


def sayDate():
    return ("today is " + str(datetime.date.today()))


def openApp(query):
    try:
        a.open(query[5:], match_closest=True, throw_error=True)
        say(f"opening {query[5:]} sir")
    except:
        if E.openSites(query):
            return
        E.searchFor(query)
        return


def vscodeOpened():
    query = takecommand()
    isExit()
    if "create" in query.lower():
        with p.hold("ctrl"):
            p.press("n")
        say("creating new file sir..")
        query = takecommand()
        isExit(query)
        if "code" in query.lower() or "write" in query.lower():
            say("wait few seconds , your program is getting ready sir")
            response = E.chat(query, "", prg=True)
            # print(response)
            p.write("#" + response)
            say(response[0])
        query = takecommand()
        isExit(query)

        if "name" in query.lower():
            x = query.split()
            filename = x[-1]
            say(f"file is named as {filename}")
            with p.hold("ctrl"):
                p.press("s")
            time.sleep(1)
            p.write(filename)
            p.press("enter")


def closeApp(query):
    say(f"closing {query[6:-4]} sir")
    a.close(query[6:-4].lower(), match_closest=True)


def sayTime():
    current_time = datetime.datetime.now().strftime("%H")
    current_time_min = datetime.datetime.now().strftime("%M")
    return (f"time is {current_time}hours {current_time_min}mins")
