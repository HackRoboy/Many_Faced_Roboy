#!/bin/bash

Roboy_IP = "10.183.113.58"
export ROS_IP="$ROBOY_IP" # make sure you are on the same network as Roboy
export ROS_HOSTNAME="$ROBOY_IP"
export ROS_MASTER_URI="http://$ROBOY_IP:11311"

rosservice call /recognize_face "object_id: 0" # to recognize the closest face
