#!/usr/bin/env python3

import rospy
from opensimrt_msgs.srv import LabelsSrv
from std_srvs.srv import Empty
rospy.init_node("commander")

read_labels = rospy.ServiceProxy("/ik/outlabels", LabelsSrv)
start_ik_srv = rospy.ServiceProxy("/inverse_kinematics_from_file/start", Empty)
start_moticon_srv = rospy.ServiceProxy("/moticon_insoles/start_playback", Empty)

rospy.sleep(3)
read_labels()
rospy.sleep(0.2)
start_ik_srv()
start_moticon_srv()
