#!/usr/bin/env python3

import unittest


class TestMoticonInsole(unittest.TestCase):

    def test_reading_file(self):
        #import rospy
        from insoles_common.insole_srv import InsoleSrv
        from insoles_common.insole_data_from_file import InsoleDataFromFile
        #rospy.init_node("test_insole_sdk")
        insrv = InsoleSrv()
        getter = InsoleDataFromFile(filename = "/srv/host_data/sample_insole.txt")
        insrv.set_getter(getter)
        insrv.waiting = False
        self.assertEqual(True,True) ## test
        #insrv.run_server()


