#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist   #To import the message type used by turtle1/cmd_vel   ---> also need to add a dependancy to package.xml

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("node has been started")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # create a message to send
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        # publish cmd_vel
        pub.publish(msg)

        rate.sleep()

