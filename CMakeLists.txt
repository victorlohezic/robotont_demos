cmake_minimum_required(VERSION 2.8.3)
project(robotont_demos)

find_package(catkin REQUIRED COMPONENTS
  robotont_msgs
  roscpp
  rospy
  std_msgs
  sensor_msgs
)

catkin_package()

