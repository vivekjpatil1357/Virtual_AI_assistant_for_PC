import datetime
import pythoncom
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import speech_recognition as sr
import win32com.client
import pyautogui as p
from plyer import notification
from config import apikey
import time
import screen_brightness_control as sbc
import external as E
import winsound
import AppOpener as a
from app import app
import pyperclip

# from main import say


def playSound():
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def adjustBrightness(value):
    value=sbc.get_brightness()[0]+value
    sbc.set_brightness(value)
    
    return f"set to {value}"

def adjustVolume(volume_level):
    pythoncom.CoInitialize()
    current_volume=0
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = int(volume.GetMasterVolumeLevelScalar()*100)
        # print(current_volume*100)
        volume.SetMasterVolumeLevelScalar((current_volume+volume_level)/100, None)
        playSound()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Uninitialize COM when done
        pythoncom.CoUninitialize()
    
    return f"set to {current_volume}"
    

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
    return "Time over sir"


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
    return "today is " + str(datetime.date.today())


def openApp(query, source):
    try:
        a.open(query, match_closest=True, throw_error=True)

        say(f"opening {query[5:]} sir")
        # if query[5:].lower()=='visual studio code':
        #     vscode(source)
    except:
        if "app" in query.lower():
            say(f"{query[5:]} not found sir")
        else:
            if E.openSites(query):
                return
            E.searchFor(query)
        return


def formatCode():
    with p.hold("ctrl"):
        p.keyDown("alt")
        p.press("f")
        p.keyUp("alt")


def toFileExplorer():
    with p.hold("ctrl"):
        p.keyDown("shift")
        p.press("p")
        p.keyUp("shift")
    p.press("enter")


def solveError(query):

    with p.hold("ctrl"):
        p.press("a")
    with p.hold("ctrl"):
        p.press("c")
    p.press("left")
    query = pyperclip.paste() + "\n" + query
    print(query)
    x = E.chat(
        query=query
        + "return only code, not explanation,no output , just corrected code",
        chatStr="",
        prg=True,
    )
    toFileExplorer()
    with p.hold("shift"):
        p.keyDown("alt")
        p.press("c")
        p.keyUp("alt")
    filename = pyperclip.paste()
    f = open(filename, "w")
    print(filename)
    f.write(x)
    f.close()
    formatCode()


def writeCode(query):
    toFileExplorer()

    with p.hold("shift"):
        p.keyDown("alt")
        p.press("c")
        p.keyUp("alt")
    filename = pyperclip.paste()
    f = open(filename, "w")
    print(filename)
    x = E.chat(
        query=query
        + "give complete code only  no comments , no explanation , no output"
        + "filename is "
        + filename,
        chatStr="",
        prg=True,
    )
    f.write(x)
    f.close()
    formatCode()


def newFile(query, langs, source):

    with p.hold("ctrl"):
        p.press("n")
    with p.hold("ctrl"):  # saving file
        p.press("s")
    time.sleep(0.1)
    p.press("tab", presses=3)
    p.press("enter")
    x = query.lower().split()
    time.sleep(0.1)
    with p.hold("ctrl"):
        p.press("k")

    p.press("m")
    global lang
    lang = "txt"
    for i in x:
        if i in langs:
            p.write(i)
            lang = i
            time.sleep(0.1)
            p.press("enter")
            toFileExplorer()
            p.press("f2")  # rename to
            with p.hold("ctrl"):
                p.press("right", presses=2)
            time.sleep(3)
            with p.hold("ctrl"):
                p.keyDown("shift")
                p.press("left", presses=5)
                p.keyUp("shift")
            time.sleep(0.4)
            p.write("first." + lang)
            p.press("enter")
            if source == "voice":
                say(f"new {i} file opened in new folder named as new at desktop sir")
                return ''
            else:
                return f"new {i} file opened"
            break
    else:
        p.write("txt")
        p.press("enter")
        if source == "voice":
            say(f"new  text opened sir")
            return ''
        else:
            return f"new textfile opened"


def renameFile(query, source):
    toFileExplorer()
    p.press("f2")  # rename to
    with p.hold("ctrl"):
        p.keyDown("shift")
        p.press("right", presses=2)
        p.keyUp("shift")
    p.write(query.split()[-1])
    p.press("enter")
    if source == "voice":
        say("file renamed to " + query.split()[-1])
        return ''
    else:
        return "file renamed to " + query.split()[-1]


def vscode(source, query):

    filename = "first.txt"
    isExit(query=query)
    if "python" in query.lower():
        query = query.lower().replace("python", "py") 
        print(query)# for .py extention
    elif "javascript" in query.lower():
        query = query.replace("javascript", "js")  # for .js extention
    print("in vscode")
    langs = ["py", "c", "java", "html", "css", "js", "php"]
    if "new " in query.lower():
        time.sleep(1)
        if source != "voice":
            with p.hold("alt"):
                p.press("tab")
            time.sleep(0.2)
        return newFile(query=query, langs=langs, source=source)
    elif "write" in query.lower() and (
        "code" in query.lower() or "program" in query.lower()
    ):  # writing code in given language
        if source != "voice":
            with p.hold("alt"):
                p.press("tab")
            time.sleep(0.2)
        writeCode(query)
        return "Code written"
    elif "rename file" in query.lower():
        if source != "voice":
            with p.hold("alt"):
                p.press("tab")
            time.sleep(0.2)
        return renameFile(query, source=source)
    elif "solve" in query.lower() and "error" in query.lower():
        if source != "voice":
            with p.hold("alt"):
                p.press("tab")
            time.sleep(0.2)
        solveError(query=query)
        with p.hold("ctrl"):
            p.keyDown("shift")
            p.press("e")
            p.keyUp("shift")
            time.sleep(0.2)
        formatCode()
        return ""
    else:
        return None


def closeApp(query):
    say(f"closing {query[6:-4]} sir")
    a.close(query[6:-4].lower(), match_closest=True)
    return "closing app sir"


def sayTime():
    current_time = datetime.datetime.now().strftime("%H")
    current_time_min = datetime.datetime.now().strftime("%M")
    return f"time is {current_time}hours {current_time_min}mins"
