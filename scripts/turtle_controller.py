#!/usr/bin/env python3
import rospy

# SUBSCRIBER
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist   #To import the message type used by turtle1/cmd_vel   ---> also need to add a dependancy to package.xml
from turtlesim.srv import SetPen

previous_x = 0

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen) # Creates a proxy of SetPen object
        response = set_pen(r, g, b, width, off) # Initialised instance of SetPen
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(pose: Pose):  #  ": Pose just tells us that the message is of type 'Pose' which allows for intellisense to work"
    """Callback function: run everytime subscriber picks up a message"""
    cmd = Twist()
    if (pose.x > 9.0) or (pose.x < 2.0) or (pose.y > 9.0) or (pose.y < 2.0):
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    pub.publish(cmd)
    
    global previous_x
    if pose.x >= 5.5 and previous_x < 5.5:
        previous_x = pose.x
        rospy.loginfo("Set color to red")
        call_set_pen_service(255, 0, 0, 4, 0)
    elif pose.x < 5.5 and previous_x >= 5.5:
        previous_x = pose.x
        rospy.loginfo("Set color to green")
        call_set_pen_service(0, 255, 0, 4, 0)


if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen")
    call_set_pen_service(255, 0, 0, 4, 0)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Node has been started")

    rospy.spin()