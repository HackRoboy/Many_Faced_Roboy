import subprocess
from logs import log
from time import sleep
import threading, sys
import flaskapp

def roboy_say(text:str):
    #return
    #text = "A. " + text 
    log.info("ROBOYSAY: " + text)
    #text = text.replace("'", "\\'")
    out_string = subprocess.check_output(["./roboy_interface.sh", "speech_synthesis", text]).decode("ascii")
    print(out_string)


catstate = False
def roboy_emotion(state:bool):
    global catstate
    if state == catstate:
        return
    catstate = state
    #return
    #text = "A. " + text 
    log.info("ROBOYEMOTION")
    #text = text.replace("'", "\\'")
    out_string = subprocess.check_output(["./roboy_interface.sh", "show_emotion", "catiris"]).decode("ascii")
    print(out_string)


def roboy_detect_speech():
    log.info("ROBOYLISTENING")
    #text = text.replace("'", "\\'")
    out_string = subprocess.check_output(["./roboy_interface.sh speech_recognition"], shell=True).decode("ascii")
    print(out_string, file=sys.stderr)
    if "Service call failed" in out_string:
        return None
    return out_string

def roboy_detect_face():
    #print("Checking Face")
    out_string = subprocess.check_output(["./roboy_interface.sh face_detection"], shell=True).decode("ascii")
    #print(out_string)
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
            sleep(0.5)
    
    t = threading.Thread(target=worker)
    t.start()