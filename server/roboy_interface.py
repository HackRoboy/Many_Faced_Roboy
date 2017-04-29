import logging
from logs import log
import subprocess
import json
import threading
import time
import flaskapp

def roboy_say(text):
	log.info("ROBOYSAY: " + text)
	return
	return subprocess.check_output(["./bashs/speech_syn.sh " + text], shell=True)

def roboy_emote(emote):
	return subprocess.check_output(["./bashs/emote.sh " + emote], shell=True)

def roboy_receive_speech():
	return subprocess.check_output(["./bashs/speech_rec.sh "], shell=True)

def roboy_face_in_field():
	return subprocess.check_output(["./bashs/contains_face.sh "], shell=True)

def roboy_rec_closest_face():
	return subprocess.check_output(["./bashs/rec_face.sh " + text], shell=True)

def test():
	return subprocess.check_output(["./bashs/test.sh "], shell=True)

def check_face():
	face_in = False
	while True:
		nface_in = "True" in roboy_face_in_field()
		if nface_in != face_in:
			flaskapp.process_updates([flaskapp.make_rupdate("fo5cus", {"val":nface_in})])
		face_in = nface_in
		time.sleep(1)

def main():
	t = threading.Thread(target=check_face)
	t.start()
	pass

"""
roboy_con = Roboy_Connector()

#Main Loop/Listener?

json_data = 1 #receive Json Object
output = ""

operation = json_data["operation"]
action = json_data["action"]

if operation=="talk":
	roboy_con.roboy_says(action)

elif operation=="emote":
	roboy_con.roboy_emote(action)

elif operation=="speech_recognition"
	output = roboy_con.roboy_receive_speech()

elif operation=="contains_face"
	output = roboy_con.roboy_face_in_field()

elif operation=="closest_face":
	output = roboy_con.roboy_rec_closest_face()

elif operation=="test":
	output = roboy_con.test()

json_prelim = {"output": output}

json_data = json.dumps(data)

#send data
"""