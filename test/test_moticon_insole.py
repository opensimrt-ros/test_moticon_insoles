#!/usr/bin/env python3

import unittest


class TestMoticonInsole(unittest.TestCase):

    def test_reading_file(self):
        #import rospy
        import insoles_common
        #rospy.init_node("test_insole_sdk")
        insrv = insoles_common.InsoleSrv()
        getter = insoles_common.InsoleDataFromFile(filename = "/catkin_ws/Data/ruoli/ViconData/Ruoli/Moticon_insole/RealTimekIDS2/walking01_header_corrected.txt")
        insrv.set_getter(getter)
        insrv.waiting = False
        self.assertEqual(True,True) ## test
        #insrv.run_server()


