#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg: Pose):  #  ": Pose just tells us that the message is of type 'Pose' which allows for intellisense to work"
    """Callback function: run everytime subscriber picks up a message"""
    rospy.loginfo(f"({msg.x} , {msg.y})")
    

if __name__ == '__main__':
    rospy.init_node("turle_pose_subscriber")

    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Node has been started")

    rospy.spin()