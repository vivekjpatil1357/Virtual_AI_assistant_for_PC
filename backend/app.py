from flask import Flask, jsonify, request
import internal as I
import external as E
import keyboard
import builtins

app = Flask(__name__)



@app.route("/say", methods=["POST"])
def say():
    d = request.get_json()
    I.say(d["text"])
    return jsonify(
        {
            "h": "",
        }
    )


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
    r = builtins.open("C:\\Users\\vivek\\OneDrive\\Desktop\\prj\\backend\\data.txt", "r")
    chatStr = r.read()
    r.close()
    x = E.chat(
        d["query"],
        chatStr=chatStr,
    )
    data = {
        "response": x,
    }
    # print("\n\n\\nn\n\n\n")
    return jsonify(data)


# chatStr=''
@app.route("/start/chat", methods=["POST"])
def chat():
    d = request.get_json()
    r = builtins.open("C:\\Users\\vivek\\OneDrive\\Desktop\\prj\\backend\\data.txt", "r")
    chatStr = r.read()
    r.close()
    d = mainalgo("chat", d["text"])
    return d


@app.route("/start/voice")
def voice():
    r = builtins.open("C:\\Users\\vivek\\OneDrive\\Desktop\\prj\\backend\\data.txt", "r")
    chatStr = r.read()
    chatStr += "\n"
    r.close()
    d = mainalgo("voice", "")
    return d

@app.route("/stop")
def stop():
    import os
    os.system('taskkill /F /PID ' + str(os.getpid()))
    


def mainalgo(source, text=""):
    if source == "voice":
        while True:
            print("Listening.......")
            query = I.takecommand()
            if "exit" in query:
                I.say("exiting sir.....")
                break
            x = ""
            if "search for" in query.lower():
                E.searchFor(query)
            elif "open" in query.lower():
                I.openApp(query=query)
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
                    "response": x['response'],
                    "imageUrl": x["imageUrl"],
                }
                return jsonify(data)
            elif (
                "adjust sound" in query.lower()
                or "increase brightness" in query.lower()
                or "decrease brightness" in query.lower()
            ):
                if "increase" in query.lower():
                    data = {"brightness": "10"}
                elif "decrease" in query.lower():
                    data = {"brightness": "-10"}
                else:
                    data = {"brightness": "adjustable"}
                return jsonify(data)
            elif (
                "adjust sound" in query.lower()
                or "increase sound" in query.lower()
                or "decrease sound" in query.lower()
            ):
                if "increase" in query.lower():
                    data = {"sound": "10"}
                elif "decrease" in query.lower():
                    data = {"sound": "-10"}
                else:
                    data = {"sound": "adjustable"}
                return jsonify(data)
            else:
                data = {"isExit": "No", "isAi": "yes", "query": query}
                return jsonify(data)

            data = {"isExit": "No", "isAi": "No", "query": query, "response": x}
            return jsonify(data)

        data = {"query": query, "isExit": "Yes", "response": "exiting sir"}

        r = builtins.open("C:\\Users\\vivek\\OneDrive\\Desktop\\prj\\backend\\data.txt", "w")
        r.write("")
        r.close()
        return jsonify(data)
    else: 

        query = text
        if "search for" in query.lower():
            x=E.searchFor(query)
        elif "open" in query.lower():
           x= I.openApp(query=query)
        elif "close" in query.lower():
            x=I.closeApp(query=query)
        elif "timer" in query.lower():
            strs = query.split(" ")
            x=I.timer(int(strs[-2]))
        elif "time" in query.lower():
            x = I.sayTime()
        elif "weather" in query.lower():
            x = E.sayWeather()
        elif "today's date" in query.lower():
            x = I.sayDate()
        elif "play" in query.lower():
            x=E.playMusic(query)
            # keyboard.wait("space")
        elif "news of" in query.lower():
            try:
                x = E.news(query=query)
            except:
                return jsonify({'response':'News not found'})
            print(x)
            data = {"isAi": "no", "response": x['response'],'isNews':'yes','imageUrl':x['imageUrl']}
            return jsonify(data)
        elif (
            "adjust sound" in query.lower()
            or "increase brightness" in query.lower()
            or "decrease brightness" in query.lower()
        ):
            if "increase" in query.lower():
                data = {"brightness": "10"}
            elif "decrease" in query.lower():
                data = {"brightness": "-10"}
            else:
                data = {"brightness": "adjustable"}
            return jsonify(data)
        elif (
            "adjust sound" in query.lower()
            or "increase sound" in query.lower()
            or "decrease sound" in query.lower()
        ):
            if "increase" in query.lower():
                data = {"sound": "10"}
            elif "decrease" in query.lower():
                data = {"sound": "-10"}
            else:
                data = {"sound": "adjustable"}
            return jsonify(data)
        else:
            data = {"isAi": "yes", "query": query}
            return jsonify(data)
        data = {"isAi": "no", "response": x}
        print(x)
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=1000)
