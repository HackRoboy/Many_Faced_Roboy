#!/bin/bash

RIP=10.183.113.58
source ~/catkin_ws/devel/setup.sh
export ROS_IP=$RIP
export ROS_HOSTNAME=$RIP
export ROS_MASTER_URI=http://$RIP:11311
export PYTHONEXE=/usr/bin/python
#echo $ROS_MASTER_URI
argv1=$1

#echo True


if [ $# -eq 2 ]
  then
	#echo "python roboy_interface.py $1 $2"
    $PYTHONEXE roboy_interface2.py $1 "$2"
  else
	#echo "python roboy_interface.py $1"
    $PYTHONEXE roboy_interface2.py $1
fi

