#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

length = 0
width = 0
def length_callback(data):
  length = data.data

def width_callback(data):
  width = data.data
  
#ROS Code

rospy.init_node("micro_rov")

pub = rospy.Publisher('mussels', Int16, queue_size=10)
rospy.Subscriber("length", Int16, length_callback)
rospy.Subscriber("width", Int16, width_callback)	

while not rospy.is_shutdown():
  pub.publish(length * width)

  time.sleep(0.01)
