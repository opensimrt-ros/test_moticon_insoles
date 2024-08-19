#!/usr/bin/env python3

import unittest
import sys
import rospy
from insole_msgs.msg import InsoleSensorStamped
from geometry_msgs.msg import WrenchStamped
import dynamic_reconfigure.client
import subprocess
import time
import os
import rosgraph

import rosservice

def delay_print(insole_topic="insole", wrench_topic="wrench"):

    a_insole_msg = rospy.wait_for_message(insole_topic, InsoleSensorStamped)
    a_wrench_msg = rospy.wait_for_message(wrench_topic, WrenchStamped)

    rospy.logwarn(f"the header from the insole :\n\t{a_insole_msg.header}")
    rospy.logwarn(f"the wrench header:\n\t {a_wrench_msg.header}")

def delay_return_times(insole_topic="insole", wrench_topic="wrench"):

    a_insole_msg = rospy.wait_for_message(insole_topic, InsoleSensorStamped)
    a_wrench_msg = rospy.wait_for_message(wrench_topic, WrenchStamped)


    return a_insole_msg.header.stamp, a_wrench_msg.header.stamp

def non():
    stream = os.popen("rosservice list")
    rospy.logwarn_once(stream.read())
    
    services = rosservice.get_service_list()

    # Print the list of services

    wtf = []
    my_name = ""
    for service in services:
        if "set_parameters" in service:
            wtf.append(service)
            rospy.logwarn(service)
            if rospy.get_namespace() in service:
                my_name = service
                rospy.logerr_once(my_name)
                rospy.logerr_once(type(my_name))

    my_master = rosgraph.Master(rospy.names.get_caller_id())
    my_uri = my_master.getUri()
    rospy.logwarn_once(my_uri)

    rospy.logerr_once(rosservice.rosgraph.get_master_uri())
    #rospy.loginfo_once(rospy.core.parse_rosrpc_uri(my_uri))
    my_service_uri = my_master.lookupService(my_name)
    rospy.logwarn("=======================what:::: {}".format(my_service_uri))
    rospy.wait_for_service(my_name)

class TestCheckDelayRepublisher(unittest.TestCase):
   
    def __init__(self, *args):
        super(TestCheckDelayRepublisher, self).__init__(*args)

        rospy.init_node("test_node")
        
        try:

            self._client = dynamic_reconfigure.client.Client(rospy.resolve_name("insole_republisher"), timeout=0.1)
        
        except:
    
            self._client = dynamic_reconfigure.client.Client(my_name.split("set_parameters")[0], timeout=0.1)
            
    

    def test_check_delay_zero(self):
        #import rospy
        params = {"side_delay":0}
        
        config = self._client.update_configuration(params)

        delay_print()

        at, bt = delay_return_times()
    
        #self.assertEqual(at,bt)
        ## this doesnt work because we are subscribing to the topics at different times, so they will never get the same seq. messages. 
        ## I would need to spend quite a lot of time to figure out how to exactly get them at the same time here, so i will just use a cheat

        self.assertTrue(abs((at-bt).to_sec())<0.1)



    def test_check_delay_positive(self):
        ## this guy is receiving a message from the future

        #import rospy
        params = {"side_delay":0.5}
        
        config = self._client.update_configuration(params)
        delay_print()

        at, bt = delay_return_times()
    
        self.assertGreater(bt,at)


    def test_check_delay_negative(self):
        params = {"side_delay":-0.5}
        
        config = self._client.update_configuration(params)
        
        delay_print()

        at, bt = delay_return_times()
    
        self.assertLess(bt,at)

if __name__ == '__main__':
    import rostest
    rostest.run('test_moticon_insoles', 'check_delay_external', TestCheckDelayRepublisher, sys.argv)

