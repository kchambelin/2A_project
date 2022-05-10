#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import time

def send_init():
    pub = rospy.Publisher('get_initialization', String, queue_size=10)
    message = 'OK'
    rospy.loginfo(message)
    time.sleep(0.1)
    pub.publish(message)

def callback(data):
    if data.data == 'Initiliaze' :
        send_init()
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('get_init', anonymous=True)

    rospy.Subscriber("initialization", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()