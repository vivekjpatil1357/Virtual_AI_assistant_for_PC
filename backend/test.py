import keyboard
import sys
from internal import say
import os

def exit_terminal():
    os.system('taskkill /F /PID ' + str(os.getpid()))


    # elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    #     os.system('kill -9 ' + str(os.getpid()))
    # else:
    #     print("Unsupported operating system. Exiting without terminal termination.")
    #     sys.exit(1)

def on_key_event(e):
    if e.name == 'q':
        exit_terminal()
        
keyboard.on_press(on_key_event)
say("helee ad kajd alj lajdfladjk ;ddj df;adfjf  ")

