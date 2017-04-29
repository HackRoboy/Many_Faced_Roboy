#!/bin/bash

source /opt/ros/kinetic/setup.bash
Roboy_IP="10.183.113.58"
text=$1

export ROS_IP=$ROBOY_IP # make sure you are on the same network as Roboy
export ROS_HOSTNAME=$ROBOY_IP
export ROS_MASTER_URI=http://$Roboy_IP:11311

rosservice call /speech_synthesis/talk "text: '$1'"
