#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import time

def callback4(data):
    if data.data == 'DONE !' :
        rospy.loginfo('DONE !')

def reproduce(positions):
    message = positions
    rospy.loginfo(message)
    pub_mvmt.publish(message)
    rospy.loginfo('Doing something')

def callback3(data) :
    'Since the only scenario is reproduce, I only take the position, not the shape or the color here.'
    positions = data.data
    rospy.loginfo('Pieces positions: ' + positions)
    reproduce(positions)

def ask_cam() :
    message = 'go'
    rospy.loginfo('Asking for cam data')
    pub_cam.publish(message)

def callback2(data):
    if data.data == 'REPRODUCE !' :
        rospy.loginfo('The order is REPRODUCE')
        ask_cam()

def ask_for_order():
    message = 'Waiting for order...'
    rospy.loginfo(message)
    pub_voice_reco.publish(message)

def callback(data):
    if data.data == 'INITIALIZE !' :
        rospy.loginfo('INITIALIZE')
        ask_for_order()

def initialize():
    message = 'Initialize'
    rospy.loginfo(message)
    pub_voice_reco.publish(message)

if __name__ == '__main__':
    try:
        rospy.init_node('main', anonymous=True)
        positions = ''
        pub_voice_reco = rospy.Publisher('main_voice_reco', String, queue_size=10)
        pub_mvmt = rospy.Publisher('main_mvmt', String, queue_size=10)
        pub_cam = rospy.Publisher('main_cam', String, queue_size=10)

        rospy.Subscriber("voice_reco_main", String, callback)
        rospy.Subscriber("voice_reco_main_order", String, callback2)
        rospy.Subscriber("cam_main", String, callback3)
        rospy.Subscriber("mvmt_main", String, callback4)

        time.sleep(2)
        print('Main here')
        initialize()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass