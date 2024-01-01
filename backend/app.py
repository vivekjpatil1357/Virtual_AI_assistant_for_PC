from flask import Flask, jsonify, request
import internal as I
import external as E
import keyboard
import builtins
app = Flask(__name__)

@app.route("/say", methods=["POST"])
def say():
    d=request.get_json()
    I.say(d['text'])
    return jsonify({'h':'',})

@app.route("/ai", methods=["POST"])
def req():
    d = request.get_json()
    r = builtins.open("data.txt", "r")
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
@app.route("/start/voice")
def voice():
    r = builtins.open("data.txt", "r")
    chatStr = r.read()
    chatStr += "\n"
    r.close()
    while True:
        print("Listening.......")
        query = I.takecommand()
        if "exit" in query:
            I.say("exiting sir.....")
            break
        x=''
        if "search for" in query.lower():
            E.searchFor(query)
        elif "open" in query.lower():
            I.openApp(query=query)
        elif "close" in query.lower():
            I.closeApp(query=query)
        elif "timer" in query:
            strs = query.split(" ")
            x=I.timer(int(strs[-2]))
        elif "time" in query:
            x=I.sayTime()
        elif "weather" in query:
            x=E.sayWeather()
        elif "today's date" in query:
            x=I.sayDate()
        elif "play" in query:
            E.playMusic(query)
            keyboard.wait("space")
        else:
            data = {"isExit": "No",'isAi':'yes', "query": query}
            return jsonify(data)
        
        data = {"isExit": "No",'isAi':'No', "query": query,"response":x}
        return jsonify(data)
        

    data = {"query": query, "isExit": "Yes", "response": "exiting sir"}

    r = builtins.open("data.txt", "w")
    r.write("")
    r.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=1000)

