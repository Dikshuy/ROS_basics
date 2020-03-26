#! /usr/bin/env python

import rospy                               # Import the Python library for ROS
import math
from geometry_msgs.msg import Twist           # Import the Int32 message from the std_msgs package
from sensor_msgs.msg import LaserScan

def callback(msg):

	if msg.ranges[320] > 1 or math.isnan(msg.ranges[320]):
		move.linear.x=2
		move.angular.z=0.0

	if msg.ranges[320] < 1:
		move.linear.x =0.1
		move.angular.z = .2

	if msg.ranges[639] < .3:
		move.linear.x=0.1
		move.angular.z=-0.2

	if msg.ranges[0] < .3:
		move.linear.x=0.1
		move.angular.z=0.2

	pub.publish(move)

rospy.init_node("move_risc")
sub = rospy.Subscriber("/scan",LaserScan,callback)
pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size = 1)
move = Twist()

rospy.spin()
