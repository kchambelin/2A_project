#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import time

def talker_init():
    pub = rospy.Publisher('voice_reco_main', String, queue_size=10)
    message = 'INITIALIZE !'
    rospy.loginfo(message)
    time.sleep(0.1)
    pub.publish(message)

def talker_reprod():
    pub = rospy.Publisher('voice_reco_main_order', String, queue_size=10)
    message = 'REPRODUCE !'
    rospy.loginfo(message)
    time.sleep(0.1)
    pub.publish(message)
    rospy.loginfo('ok')

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    order = data.data.split(",")
    if order[0]=='begin' or order[0] == 'initialise':
        rospy.loginfo('initialisation')
        talker_init()
    elif order[0] == 'reproduce' or order[0] == 'go':
        rospy.loginfo('reproduce')
        talker_reprod()
   
def listener():

    rospy.init_node('voice_reco_listener', anonymous=True)

    rospy.Subscriber('voice_reco', String, callback)

    rospy.spin()
    
if __name__ == '__main__':
    listener()
