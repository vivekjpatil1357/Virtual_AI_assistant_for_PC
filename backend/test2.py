import pyautogui as p
import AppOpener as a
import time
from external import chat
from internal import takecommand
import pyperclip
import internal as I


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
    x = chat(
        query=query
        + "return only code, not explanation,no output , just corrected code",
        chatStr="",
        prg=True,
    )
    toFileExplorer()
    with p.hold("shift"):
        p.keyDown('alt')
        p.press("c")
        p.keyUp('alt')
    filename=pyperclip.paste()
    f = open(filename, "w")
    print(filename)
    f.write(x)
    f.close()
    formatCode()

def writeCode(query):
    toFileExplorer()
    
    with p.hold("shift"):
        p.keyDown('alt')
        p.press("c")
        p.keyUp('alt')
    filename=pyperclip.paste()
    f = open(filename, "w") 
    print(filename)
    x = chat(
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


def newFile(query, langs,source):

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
            with p.hold("ctrl"):
                p.keyDown("shift")
                p.press("left", presses=5)
                p.keyUp("shift")
            p.write("first." + lang)
            p.press("enter")
            if source=='voice':
                 I.say(f"new {i} file opened in new folder named as new at desktop sir")
            else:
                return f'new {i} file opened'
            break
    else:
        p.write("txt")
        p.press("enter")
        if source=='voice':
                 I.say(f"new text opened sir")
        else:
            return f'new textfile opened'


def renameFile(query,source):
    toFileExplorer()
    p.press("f2")  # rename to
    with p.hold("ctrl"):
        p.keyDown("shift")
        p.press("right", presses=2)
        p.keyUp("shift")
    p.write(query.split()[-1])
    p.press("enter")    
    if source=='voice':
        I.say("file renamed to " + query.split()[-1])
    else:
        return "file renamed to " + query.split()[-1]


def vscode(source,query):

        filename = "first.txt"
        I.isExit(query=query)
        if "python" in query.lower():
            query = query.replace("python", "py")  # for .py extention
        elif "javascript" in query.lower():
            query = query.replace("javascript", "js")  # for .js extention
        print('in vscode')

        langs = ["py", "c", "java", "html", "css", "js", "php"]

        if "new " in query.lower():
            time.sleep(1)
            with p.hold("alt"):
                p.press("tab")
                time.sleep(0.2)
            return newFile(query=query, langs=langs,source=source)
        elif "write" in query.lower() and (
            "code" in query.lower() or "program" in query.lower()
        ):  # writing code in given language
            with p.hold("alt"):
                p.press("tab")
                time.sleep(0.2)
            writeCode(query)
            return 'Code written'
        elif "rename file" in query.lower():
            with p.hold("alt"):
                p.press("tab")
                time.sleep(0.2)
            return renameFile(query,source=source)
        elif "solve" in query.lower() and "error" in query.lower():
            with p.hold("alt"):
                p.press("tab")
                time.sleep(0.2)
            solveError(query=query)
            with p.hold("ctrl"):
                p.keyDown('shift')
                p.press("e")
                p.keyUp('shift')
                time.sleep(0.2)
            formatCode()
            return ''
        else :
            return None


# vscode("voice",'')
