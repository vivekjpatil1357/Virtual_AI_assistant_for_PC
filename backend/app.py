from flask import Flask, jsonify, request
import internal as I
import external as E
import keyboard
import builtins
import AppOpener as a
import psutil
import time
import pyautogui as p
import config as c

app = Flask(__name__)

@app.route("/roleplay", methods=["POST"])
def sendRes():
    print("hello i am in sendRes")
    d = request.get_json()
    print(d)
    text = d["text"]
    role = d["role"]
    desc = d["desc"]
    r = builtins.open(c.roleplay, "r")
    chatStr = r.read()
    r.close()
    x = E.roleplay(
        query=text,
        role=role,
        desc=desc,
        chatStr=chatStr,
    )
    print(chatStr)
    data = {
        "response": x,
        'role':role
    }
    # print("\n\n\\nn\n\n\n")
    return jsonify(data)


@app.route("/say", methods=["POST"])
def say():
    d = request.get_json()
    I.say(d["text"])
    return jsonify(dict())


@app.route("/brightness", methods=["POST"])
def brightness():
    d = request.get_json()
    I.adjustBrightness(d["value"])
    return jsonify(
        {
            "h": "",
        }
    )


@app.route("/volume", methods=["POST"])
def volume():
    d = request.get_json()
    I.adjustVolume(d["value"])
    return jsonify(
        {
            "h": "",
        }
    )


@app.route("/ai", methods=["POST"])
def req():
    d = request.get_json()
    r = builtins.open(c.data, "r")
    chatStr = r.read()
    r.close()
    x = E.chat(
        d["query"],
        chatStr=chatStr,
    )
    data = {
        "response": x,
    }
    return jsonify(data)


# chatStr=''
@app.route("/start/chat", methods=["POST"])
def chat():
    d = request.get_json()
    r = builtins.open(c.data, "r")
    chatStr = r.read()
    r.close()
    d = mainalgo("chat", d["text"])
    return d


@app.route("/start/voice")
def voice():
    r = builtins.open(c.data, "r")
    chatStr = r.read()
    chatStr += "\n"
    r.close()
    d = mainalgo("voice", "")
    return d


@app.route("/stop")
def stop():
    import os

    os.system("taskkill /F /PID " + str(os.getpid()))


def is_process_running(process_name):
    for process in psutil.process_iter():
        if process.name().lower() == process_name.lower():
            return True
    return False


def mainalgo(source, text=""):
    isOpened = is_process_running("Code.exe")
    if source == "voice":
        while True:
            print("Listening.......")
            query = I.takecommand()

            if "exit" in query:
                I.say("exiting sir.....")
                break
            x = ""
            e = I.vscode("voice", query)
            if e is not None:
                print("hello world")
                return jsonify(
                    {"query": query, "isAi": "no", "isExit": "No", "response": e}
                )
                # if e is not None:
                #     print('return from vscode to frontend')
                #     return
            if (
                "open vs code" in query.lower()
                or "open visual studio code" in query.lower()
            ):
                print("opening vs code through voice")
                time.sleep(0.3)
                a.open("visual studio code", match_closest=True)
                time.sleep(2)
                with p.hold("ctrl"):
                    p.press("k")
                with p.hold("ctrl"):
                    p.press("o")
                time.sleep(0.2)
                p.write("new")
                p.press("tab")
                print("now enter")
                time.sleep(2)
                p.press("enter")
                time.sleep(2)
                isOpened = True
                return jsonify(
                    {
                        "query": query,
                        "isAi": "no",
                        "isExit": "No",
                        "response": "vs code opened",
                    }
                )
            elif "search for" in query.lower():
                E.searchFor(query)
            elif "open" in query.lower():
                I.openApp(query=query, source="voice")
            elif "close" in query.lower():
                I.closeApp(query=query)
            elif "timer" in query.lower():
                strs = query.split(" ")
                x = I.timer(int(strs[-2]))
            elif "time" in query.lower():
                x = I.sayTime()
            elif "weather" in query.lower():
                x = E.sayWeather()
            elif "today's date" in query.lower():
                x = I.sayDate()
            elif "play" in query.lower():
                E.playMusic(query)
                keyboard.wait("space")
            elif "news of" in query.lower():
                x = E.news(query=query)
                data = {
                    "isExit": "No",
                    "isAi": "No",
                    "query": query,
                    "response": x["response"],
                    "imageUrl": x["imageUrl"],
                }
                return jsonify(data)
        
            elif ("increase" in query.lower() or "decrease" in query.lower()) and (
                "brightness" in query.lower()
            ):
                if "increase" in query.lower():
                    data = {"brightness": "20"}
                elif "decrease" in query.lower():
                    data = {"brightness": "-20"}
                else:
                    data = {"brightness": "adjustable"}
                return jsonify(data)
            elif ("increase" in query.lower() or "decrease" in query.lower()) and (
                "sound" in query.lower() or "volume" in query.lower()
            ):
                print("increasing")
                if "increase" in query.lower():
                    print("increasing")
                    x = I.adjustVolume(20)
                    data = {"response": x, "isExit": "No", "isAi": "no"}
                elif "decrease" in query.lower():
                    x = I.adjustVolume(-20)

                    data = {"response": x, "isExit": "No", "isAi": "no"}
                return jsonify(data)
            else:
                data = {"isExit": "No", "isAi": "yes", "query": query}
                return jsonify(data)

            data = {"isExit": "No", "isAi": "No", "query": query, "response": x}
            return jsonify(data)

        data = {"query": query, "isExit": "Yes", "response": "exiting sir"}

        r = builtins.open(c.data, "w")
        r.write("")
        r.close()
        return jsonify(data)
    else:
        query = text
        # if isOpened:
        e = I.vscode("chat", query)
        if e is not None:
            print("hello world")
            return jsonify({"isAi": "no", "response": e})
            # if e is not None:
            #     print('return from vscode to frontend')
            #     return
        if (
            "open vs code" in query.lower()
            or "open visual studio code" in query.lower()
        ):
            time.sleep(0.3)
            a.open("visual studio code", match_closest=True)
            time.sleep(2)

            with p.hold("ctrl"):
                p.press("k")
            with p.hold("ctrl"):
                p.press("o")
            time.sleep(2)
            p.write("new")
            p.press("tab")
            print("now enter")
            time.sleep(2)
            p.press("enter")
            time.sleep(2)
            isOpened = True
            return jsonify({"isAi": "no", "response": "vs code opened"})
        elif "search for" in query.lower():
            x = E.searchFor(query)
            isOpened = False
        elif "open" in query.lower():
            x = I.openApp(query=query, source=source)
            isOpened = False
        elif "close" in query.lower():
            x = I.closeApp(query=query)
            isOpened = False
        elif "timer" in query.lower():
            strs = query.split(" ")
            x = I.timer(int(strs[-2]))
            isOpened = False
        elif "time" in query.lower():
            x = I.sayTime()
            isOpened = False
        elif "weather" in query.lower():
            x = E.sayWeather()
            isOpened = False
        elif "today's date" in query.lower():
            x = I.sayDate()
            isOpened = False
        elif "play" in query.lower():
            x = E.playMusic(query)
            isOpened = False
            # keyboard.wait("space")
        elif "news of" in query.lower():
            isOpened = False
            try:
                x = E.news(query=query)
            except:
                return jsonify({"response": "News not found"})
            print(x)
            data = {
                "isAi": "no",
                "response": x["response"],
                "isNews": "yes",
                "imageUrl": x["imageUrl"],
            }
            return jsonify(data)
        elif ("increase" in query.lower() or "decrease" in query.lower()) and (
            "brightness" in query.lower()
        ):
            isOpened = False
            if "increase" in query.lower():
                x = I.adjustBrightness(20)
            elif "decrease" in query.lower():
                x = I.adjustBrightness(-20)

        elif ("increase" in query.lower() or "decrease" in query.lower()) and (
            "sound" in query.lower() or "volume" in query.lower()
        ):
            isOpened = False
            if "increase" in query.lower():
                x = I.adjustVolume(20)

            elif "decrease" in query.lower():
                x = I.adjustVolume(-20)

        else:
            isOpened = False
            data = {"isAi": "yes", "query": query}
            return jsonify(data)
        data = {"isAi": "no", "response": x}
        print(x)
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=1000)
