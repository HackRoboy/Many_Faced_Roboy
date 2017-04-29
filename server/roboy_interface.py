import subprocess
from logs import log
from time import sleep
import threading
import flaskapp

def roboy_say(text:str):
    log.info("ROBOYSAY: " + text)
    out_string = subprocess.check_output(["python ./roboy_interface2.py speech_synthesis 'Hello World'"], shell=True) 

def roboy_detect_face():
    out_string = subprocess.check_output(["python ./roboy_interface2.py face_detection"], shell=True) 
    if "Service call failed" in out_string:
        return None
    return out_string



def main():
    def worker():
        focus = False
        while True:
            nfocus = "True" in roboy_detect_face()
            if nfocus != focus:
                flaskapp.process_updates([flaskapp.make_rupdate("focus", {"val":nfocus})])
                focus = nfocus
            sleep(1)
    
    t = threading.Thread(target=worker)
    t.start()