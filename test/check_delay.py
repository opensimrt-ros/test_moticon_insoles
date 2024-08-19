#!/usr/bin/env python3

import rospy
from insole_msgs.msg import InsoleSensorStamped
from geometry_msgs.msg import WrenchStamped

def delay_print(insole_topic="insole", wrench_topic="wrench"):


    a_insole_msg = rospy.wait_for_message(insole_topic, InsoleSensorStamped)
    a_wrench_msg = rospy.wait_for_message(wrench_topic, WrenchStamped)

    rospy.logwarn(a_insole_msg.header)
    rospy.logwarn(a_wrench_msg.header)

def delay_return_times(insole_topic="insole", wrench_topic="wrench"):

    a_insole_msg = rospy.wait_for_message(insole_topic, InsoleSensorStamped)
    a_wrench_msg = rospy.wait_for_message(wrench_topic, WrenchStamped)


    return a_insole_msg.header.stamp, a_wrench_msg.header.stamp


if __name__=="__main__":
    rospy.init_node("delay_measuring")
    delay_print()


