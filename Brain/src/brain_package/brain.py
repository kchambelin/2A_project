PKG = 'brain_package'

import roslib; roslib.load_manifest(PKG)
import rospy
from std_msgs.msg import String

def callback(data) :
    rospy.loginfo(data.data)
    if data.data == 0 :
        Initialize()
    else :
        Get_initialize_from_voc_reco()

def Get_initialize_from_voc_reco() :
    rospy.init_node('Ask_init', anonymous=True)
    pub = rospy.Publisher("Ask_for_init", String)
    rospy.loginfo("Ask_for_initialization")
    pub.publish("Ask_for_initialization")

    rospy.init_node('Answer_init', anonymous=True)
    rospy.Subscriber("Ask_for_init", String, callback)

def Initialize() :
    return


if __name__ == '__main__' :
    Get_initialize_from_voc_reco()