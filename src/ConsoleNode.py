#! /usr/bin/env python
import sys, select, tty, termios
import rospy
from std_msgs.msg import String


cmd_pub = rospy.Publisher('demo/command', String, queue_size = 1)
rospy.init_node("console")
rate = rospy.Rate(100)
old_attr = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

print "Enter Commands"
while not rospy.is_shutdown():
    inpt = raw_input('')
    cmd_pub.publish(inpt)
    rate.sleep()
termios.tcsetattr(sys.stdin, termios.TCADRIAN, old_attr)
