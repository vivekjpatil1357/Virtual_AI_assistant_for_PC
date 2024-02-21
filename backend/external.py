# from internal import say
import os
import webbrowser
import openai
from openai import OpenAI
import speech_recognition as sr
import pyautogui as p
from config import apikey
import requests
import config as c
import internal as I
import google.generativeai as genai

import builtins
import random
# def roleplay(query,role,desc,chatStr):
#     genai.configure(api_key=c.apikeyGoogle)
#     chatStr += f"Vivek: {query}\n {role}({desc}):"
#     generation_config = {
#   "temperature": 0.9,
#   "top_p": 1,
#   "top_k": 1,
#   "max_output_tokens": 2048,
# }
#     safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
# ]
#     model = genai.GenerativeModel(model_name="gemini-1.0-pro",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)
#     convo = model.start_chat(history=[
# ])
    
#     convo.send_message(chatStr)
#     chatStr += convo.last.text + "\n"
#     r = builtins.open(
#         c.roleplay, "a"
#     )
#     r.write(f"Vivek:{query}\n" +role+":"+ convo.last.text + "\n")
#     r.close()
#     print(convo.last.text)
    
#     print('from gemini')
#     return convo.last.text
def roleplay(query,role,desc,chatStr):
    openai.api_key = apikey
    chatStr += f"Vivek: {query}\n {role}({desc}):"
    client = OpenAI()
   
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct-0914",
        prompt=chatStr,
        temperature=1,
        max_tokens=1256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    chatStr += response.choices[0].text + "\n"
    r = builtins.open(
        c.roleplay, "a"
    )
    r.write(f"Vivek:{query}\n" +role+":"+ response.choices[0].text + "\n")
    r.close()
    return response.choices[0].text



def news(query):
    x = query.find("news")
    x += 8
    y = query[x:]
    print(y)
    api_url = f"https://newsapi.org/v2/everything?q={y}&sortby=relevancy&language=en&apiKey=b5beed84db25450a92ff23f6e37106bc"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        x = random.randint(0, 20)
        # print(x)
        return {
            "response": "the report of "
            + data["articles"][x]["source"]["name"]
            + " says, "
            + data["articles"][x]["description"],
            "imageUrl": data["articles"][x]["urlToImage"],
        }
    else:
        return {"response": ("there is some problem in fetching info from Api",)}


def playMusic(music):
    url = "https://spotify23.p.rapidapi.com/search/"
    querystring = {
        "q": music[4:],
        "type": "tracks",
        "offset": "0",
        "limit": "10",
        "numberOfTopResults": "1",
    }
    headers = {
        "X-RapidAPI-Key": "1b2fa80b06msh52fc3b1599c9b60p14a7f2jsn4e909b0a3c29",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    x = response.json()
    I.say("playing music sir..")
    # muteMic()
    # sr.stop()
    os.system(f"start {x['tracks']['items'][0]['data']['uri']}")
    return f"playing { music[4:]} sir"


def chat(query, chatStr, prg=False):
    openai.api_key = apikey
    chatStr += f"Vivek: {query}\n pixel(an virtual assistant made by vivek ):"
    client = OpenAI()
    if prg == True:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct-0914",
            prompt=query,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].text
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct-0914",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    chatStr += response.choices[0].text + "\n"
    r = builtins.open(
        c.data, "a"
    )
    r.write(f"Vivek:{query}\npixel:" + response.choices[0].text + "\n")
    r.close()
    return response.choices[0].text


def sayWeather():
    apiKey = "483ac82fc0db786e60a0727d2d447f1d"
    complete_url = (
        "https://api.openweathermap.org/data/2.5/weather?q=jalgaon&appid=" + apiKey
    )
    response = requests.get(complete_url)
    x = response.json()
    return f"""In the city Jalgaon, the current temperature is {int(x["main"]["temp"] - 273.55)}°C, with a {x["weather"][0]["description"]} conditions . I will suggest you to prepare accordingly for the today's weather conditions." """


def searchFor(query):
    webbrowser.open("https://www.google.com/search?q=" + query)
    I.say("here what i found on web:")
    return "here what i found on web"


def youtube(address):
    I.say(f"opening youtube sir..")
    webbrowser.open(address)
    I.say("tell me what are you searching for ")
    search = I.takecommand()
    I.say(f"searching for {search}")
    p.press("/")
    p.write(search)
    p.press("enter")


def openSites(query):
    sites = [
        ["youtube", "https://youtube.com"],
        ["wikipedia", "https://wikipedia.com"],
        ["google", "https://google.com"],
        ["meet", "https://easymeet.pythonanywhere.com"],
    ]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            I.say(f"opening {site[0]} sir")
            webbrowser.open(site[1])
            return True

    return False
