PKG = 'brain_package'

import roslib; roslib.load_manifest(PKG)
import rospy
from std_msgs.msg import String


def Get_initialize_from_voc_reco() :
    rospy.init_node('brain_voc_reco', anonymous=True)



if __name__ == '__main__' :
    Get_initialize_from_voc_reco()