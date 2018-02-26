#! /usr/bin/env python
import rospy
from std_msgs.msg import String
from summ.srv import FakeNLP

rospy.init_node("main")
print "init node"
rospy.wait_for_service('FakeNLP')
print "waiting for service"
converter = rospy.ServiceProxy('FakeNLP', FakeNLP)

def command_cb (msg):
    print msg
    radius = converter.FakeNLP(msg)
    print radius
    
rospy.Subscriber('demo/command', String, command_cb)
rospy.spin()
