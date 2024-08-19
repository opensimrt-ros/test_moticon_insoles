#!/usr/bin/env python3

import unittest

class TestCheckDelay(unittest.TestCase):


    def test_check_delay_zero(self):
        #import rospy
        from . import check_delay
        import rospy
        from insole_msgs.msg import InsoleSensorStamped
        from geometry_msgs.msg import WrenchStamped

        rospy.init_node("test_node", anonymous=True)
        ip = rospy.Publisher("insole", InsoleSensorStamped, queue_size=1, latch=True)
        wp = rospy.Publisher("wrench", WrenchStamped, queue_size=1, latch=True)


        aimsg = InsoleSensorStamped()
        now =rospy.Time.now() 
        aimsg.header.stamp = now
        awmsg = WrenchStamped()
        awmsg.header.stamp = now

        ip.publish(aimsg)
        wp.publish(awmsg)

        check_delay.delay_print()

        at, bt = check_delay.delay_return_times()
    
        self.assertEqual(at,bt)



    def test_check_delay_positive(self):
        ## this guy is receiving a message from the future

        #import rospy
        from . import check_delay
        import rospy
        from insole_msgs.msg import InsoleSensorStamped
        from geometry_msgs.msg import WrenchStamped

        rospy.init_node("test_node", anonymous=True)
        ip = rospy.Publisher("insole", InsoleSensorStamped, queue_size=1, latch=True)
        wp = rospy.Publisher("wrench", WrenchStamped, queue_size=1, latch=True)


        now =rospy.Time.now() 
        aimsg = InsoleSensorStamped()
        aimsg.header.stamp = now
        awmsg = WrenchStamped()
        awmsg.header.stamp = now + rospy.Duration(5)

        ip.publish(aimsg)
        wp.publish(awmsg)

        #check_delay.delay_print()

        at, bt = check_delay.delay_return_times()
    
        self.assertGreater(bt,at)


        #insrv.run_server()

    def test_check_delay_negative(self):
        #import rospy
        from . import check_delay
        import rospy
        from insole_msgs.msg import InsoleSensorStamped
        from geometry_msgs.msg import WrenchStamped

        rospy.init_node("test_node", anonymous=True)
        ip = rospy.Publisher("insole", InsoleSensorStamped, queue_size=1, latch=True)
        wp = rospy.Publisher("wrench", WrenchStamped, queue_size=1, latch=True)


        now =rospy.Time.now() 
        aimsg = InsoleSensorStamped()
        aimsg.header.stamp = now
        awmsg = WrenchStamped()
        awmsg.header.stamp = now - rospy.Duration(5)

        ip.publish(aimsg)
        wp.publish(awmsg)

        #check_delay.delay_print()

        at, bt = check_delay.delay_return_times()
    
        self.assertLess(bt,at)

#if __name__ == '__main__':
#    import rostest
#    rostest.run('test_moticon_insoles', 'check_delay', TestCheckDelay, sys.argv)


