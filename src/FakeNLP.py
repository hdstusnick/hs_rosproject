#! /usr/bin/env python
import rospy, re

from summ.srv import FakeNLP, FakeNLPResponse

rospy.init_node("FakeNLP")

check = re.compile('turn:P([0-9]*)')

def fake_nlp (request):
    print "do we get here"
    print request
    print re.findall("\d+", request)
    return (float) (re.findall("\d+", request))
    
service = rospy.Service('FakeNLP', FakeNLP, fake_nlp)

rospy.spin()
