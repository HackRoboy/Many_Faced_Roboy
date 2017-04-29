#!/bin/bash

RIP=10.183.113.58
source ~/catkin_ws/devel/setup.sh
export ROS_IP=$RIP
export ROS_HOSTNAME=$RIP
export ROS_MASTER_URI=http://$RIP:11311
#echo $ROS_MASTER_URI
argv1=$1

if [ $# -eq 2 ]
  then
    argv2=$2
	#echo "python roboy_interface.py $1 $2"
    python roboy_interface2.py $1 $2
  else
	#echo "python roboy_interface.py $1"
    python roboy_interface2.py $1
fi

