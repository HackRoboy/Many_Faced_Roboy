#!/usr/bin/env python
import sys
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

global quest
global prevent_repeat
global jumped

def callback(data):
	fun = data.pose.pose.position;
	print(fun.x, fun.y, fun.z)
	if quest=="jump":
		if fun.y>1: #to change
			print "Quest done"
			prevent_repeat = True
			jump=True
		else:
			prevent_repeat = False
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("initialpose", PoseWithCovarianceStamped, callback)
    rospy.spin()

if __name__ == '__main__':
	quest = sys.argv[1]
	jump = False
	prevent_repeat = False
	listener()
