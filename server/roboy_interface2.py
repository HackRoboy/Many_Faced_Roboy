#!/usr/bin/env python

from roboy_comm.srv import *
import sys
import rospy
import pdb


#import subprocess
#example: out_string = subprocess.check_output(["python ./roboy_interface.py face_detection"], shell=True) 
#example: out_string = subprocess.check_output(["python ./roboy_interface.py speech_synthesis 'Hello World'"], shell=True) 

def speech_synthesis(text):
	print(text)
	rospy.wait_for_service("speech_synthesis/talk")
	#print("found service")
	#pdb.set_trace()
	try:
		stt = rospy.ServiceProxy('speech_synthesis/talk', Talk)
		resp = stt(text)
		print "done"
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def speech_recognition():
	#print("asdf")
	#return
	rospy.wait_for_service("TextSpoken")
	try:
		stt = rospy.ServiceProxy('TextSpoken', TextSpoken)
		resp = stt()
		print resp.text
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def face_detection():
	rospy.wait_for_service("detect_face")
	try:
		stt = rospy.ServiceProxy('detect_face', wakeup)
		resp = stt()
		print resp
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def show_emotion(emotion):
	rospy.wait_for_service("roboy_face/show_emotion")
	try:
		stt = rospy.ServiceProxy('roboy_face/show_emotion', ShowEmotion)
		resp = stt(emotion)
		print "done"
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def recorded_move(movement_value):
	rospy.wait_for_service("roboy_move/replay")
	try:
		stt = rospy.ServiceProxy('roboy_move/replay', Movement)
		resp = stt("value: " + movement_value)
		print "done"
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def head_move(movement_value):
	rospy.wait_for_service("roboy_move/yaw")
	try:
		stt = rospy.ServiceProxy('roboy_move/yaw', Movement)
		resp = stt("value: " + movement_value)
		print "done"
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e


if __name__ == "__main__":
	operation = sys.argv[1];

	if operation=="speech_synthesis":
		text = sys.argv[2];
		speech_synthesis(text)

	elif operation=="speech_recognition":
		speech_recognition()

	elif operation=="face_detection":
		face_detection()

	elif operation=="show_emotion":
		emotion = sys.argv[2]
		show_emotion(emotion)

	elif operation=="head_move":
		move_val = sys.argv[2]
		head_move(move_val)

	elif operation=="recorded_move":
		move_val = sys.argv[2]
		recorded_move(move_val)
		
