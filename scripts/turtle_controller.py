#!/usr/bin/env python3
import rospy

# SUBSCRIBER
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist   #To import the message type used by turtle1/cmd_vel   ---> also need to add a dependancy to package.xml

def pose_callback(pose: Pose):  #  ": Pose just tells us that the message is of type 'Pose' which allows for intellisense to work"
    """Callback function: run everytime subscriber picks up a message"""
    cmd = Twist()
    cmd.linear.x = 5.0
    cmd.angular.z = 0.0
    pub.publish(cmd)


if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Node has been started")

    rospy.spin()