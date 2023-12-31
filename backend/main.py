import internal as I
import external as E
import keyboard
import os
import webbrowser
import datetime
import openai
import speech_recognition as sr
import win32com.client
import pyautogui as p
from config import apikey
import time
from AppOpener import open, close
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""


def on_key_event(e):
    if e.name == 'space':
        print("Play/Pause")
# key for google engine =AIzaSyCSCX_gZ_Rky0fxjECnOuVpGH3wMt4pkJg
# engine id=e0060bbbcdf00484c


if __name__ == '__main__':
    while True:
        query = I.takecommand()
        if "hello jarvis" in query.lower():
            I.say("Hello I am Jarvis AI, welcome back master!!")
            break
    while True:
        print("Listening.......")
        query = I.takecommand()
        if "exit" in query:
            I.say("exiting sir.....")
            exit()
        elif "search for" in query.lower():
           E.searchFor(query)
        elif "open" in query.lower():
            I.openApp(query=query)
        elif "close" in query.lower():
            I.closeApp(query=query)
        elif "timer" in query:
            strs = query.split(' ')
            I.timer(int(strs[-2]))
        elif "time" in query:
            I.sayTime()
        elif "weather" in query:
            E.sayWeather()
        elif "today's date" in query:
            I.sayDate()
        elif "play" in query:
            E.playMusic(query)
            keyboard.wait('space')
        else:
            chatStr = E.chat(query, chatStr)
