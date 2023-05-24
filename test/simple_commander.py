#!/usr/bin/env python3

import rospy
from opensimrt_msgs.srv import LabelsSrv
from std_srvs.srv import Empty
rospy.init_node("commander")

start_moticon_srv = rospy.ServiceProxy("/moticon_insoles/start_playback", Empty)

rospy.sleep(3)
start_moticon_srv()
