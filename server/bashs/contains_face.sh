#!/bin/bash

source /opt/ros/kinetic/setup.bash
ROBOY_IP="10.183.113.58"

export ROS_IP=$ROBOY_IP # make sure you are on the same network as Roboy
export ROS_HOSTNAME=$ROBOY_IP
export ROS_MASTER_URI=http://$ROBOY_IP:11311

rosservice call /detect_face "{}" # to detect whether there's a face in a camera frame
