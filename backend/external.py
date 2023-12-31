# from internal import say
import pyaudio
import os
import webbrowser
import keyboard
import datetime
import openai
from openai import OpenAI
import speech_recognition as sr
import win32com.client
import pyautogui as p
from config import apikey
import time
import requests
# from AppOpener import open, close
import internal as I
import builtins


def playMusic(music):

    url = "https://spotify23.p.rapidapi.com/search/"
    querystring = {"q": music, "type": "tracks", "offset": "0",
                   "limit": "10", "numberOfTopResults": "1"}
    headers = {
        "X-RapidAPI-Key": "1b2fa80b06msh52fc3b1599c9b60p14a7f2jsn4e909b0a3c29",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    x = response.json()
    I.say("playing music sir..")
    # muteMic()
    # sr.stop()
    os.system(f"start {x['tracks']['items'][0]['data']['uri']}")
    return

def chat(query, chatStr, prg=False):
    openai.api_key = apikey
    
    chatStr += f"Vivek: {query}\n Jarvis:"
    client = OpenAI()
    
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct-0914",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if prg == True:
        return response.choices[0].text
    chatStr += response.choices[0].text + "\n"
    r = builtins.open("data.txt", "a")
    r.write(f"Vivek:{query}\nJarvis:" + response.choices[0].text + "\n")
    r.close()
    return response.choices[0].text



def sayWeather():
    apiKey = "483ac82fc0db786e60a0727d2d447f1d"
    complete_url = (
        "https://api.openweathermap.org/data/2.5/weather?q=jalgaon&appid=" + apiKey
    )
    response = requests.get(complete_url)
    x = response.json()
    return (
        f'''In the city Jalgaon, the current temperature is {int(x["main"]["temp"] - 273.55)}°C, with a {x["weather"][0]["description"]} conditions . I will suggest you to prepare accordingly for the today's weather conditions." ''')


# def google(query):
#     API_KEY = "AIzaSyCSCX_gZ_Rky0fxjECnOuVpGH3wMt4pkJg"
#     SEARCH_ENGINE_ID = "e0060bbbcdf00484c"
#     SEARCH_QUERY = query

#     BASE_URL = f"https://www.googleapis.com/customsearch/v1"

#     params = {
#         "key": API_KEY,
#         "cx": SEARCH_ENGINE_ID,
#         "q": SEARCH_QUERY
#     }

#     response = requests.get(BASE_URL, params=params)
#     data = response.json()
#     if "items" in data:
#         for item in data["items"]:
#             webbrowser.open("https://www.google.com/search?q="+item['title'])
#             break

def searchFor(query):
    webbrowser.open("https://www.google.com/search?q="+query)
    I.say("here what i found on web:")

    
def youtube(address):
    I.say(f"opening youtube sir..")
    webbrowser.open(address)

    I.say("tell me what are you searching for ")
    search = I.takecommand()
    I.say(f'searching for {search}')
    p.press('/')
    p.write(search)
    p.press("enter")


def openSites(query):
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["google", "https://google.com"], ["meet", "https://easymeet.pythonanywhere.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            I.say(f"opening {site[0]} sir")
            webbrowser.open(site[1])
            return True

    return False
