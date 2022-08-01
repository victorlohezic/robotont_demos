#! /usr/bin/python3.8

import rospy
from geometry_msgs.msg import Twist


def msgCallback(inputMsg: Twist):
    outputMsg.linear.x = 0
    outputMsg.linear.y = 0
    outputMsg.linear.z = 0
    outputMsg.angular.x = 0
    outputMsg.angular.y = 0
    outputMsg.angular.z = 0
    if inputMsg.linear.x:
        outputMsg.linear.x = inputMsg.linear.x
    elif inputMsg.linear.y:
        outputMsg.linear.y = inputMsg.linear.y
    elif inputMsg.linear.z:
        outputMsg.linear.z = inputMsg.linear.z
    elif inputMsg.angular.x:
        outputMsg.angular.x = inputMsg.angular.x
    elif inputMsg.angular.y:
        outputMsg.angular.y = inputMsg.angular.y
    elif inputMsg.angular.z:
        outputMsg.angular.z = inputMsg.angular.z
    publisher.publish(outputMsg)

if __name__ == "__main__":
    outputMsg = Twist()

    rospy.init_node('combiner', anonymous=True)

    subscriber1 = rospy.Subscriber("/twist_up", Twist, msgCallback)
    subscriber2 = rospy.Subscriber("/twist_down", Twist, msgCallback)
    subscriber3 = rospy.Subscriber("/twist_right", Twist, msgCallback)
    subscriber4 = rospy.Subscriber("/twist_left", Twist, msgCallback)
    subscriber5 = rospy.Subscriber("/twist_angular_left", Twist, msgCallback)
    subscriber6 = rospy.Subscriber("/twist_angular_right", Twist, msgCallback)
    publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    rospy.spin()
