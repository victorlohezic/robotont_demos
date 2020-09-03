# robotont\_demos
This repository is a ROS package that contains various demos showing the capabilities of the Robotont platform

[![Build Status](https://travis-ci.org/robotont/robotont_demos.svg?branch=melodic-devel)](https://travis-ci.org/robotont/robotont_demos)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Before you begin
To run the demos it is necessary to have a ROBOTONT robot and a user PC with Ubuntu Linux and ROS Melodic installed.

## 3D mapping
**Setup**<br/>

*You only need to run these commands if this is the first time you you run this demo with the current user PC or ROBOTONT on-board computer.*

On ROBOTONT on-board computer, install ROS wrapper of RTAB-Map<br/>
```sudo apt update```
```sudo apt install ros-melodic-rtabmap-ros```

**Launching the demo**<br/>

On ROBOTONT on-board computer, launch 3d_mapping.launch<br/>
```roslaunch robotont_demos 3d_mapping.launch```

On user PC, launch display_3d_mapping.launch to visualize the result<br/>
```roslaunch robotont_demos display_3d_mapping.launch```

## 2D mapping
**Setup**<br/>

*You only need to run these commands if this is the first time you you run this demo with the current user PC or ROBOTONT on-board computer.*

On ROBOTONT on-board computer, install the following packages:<br/>
```sudo apt install ros-melodic-depthimage-to-laserscan```<br/>
```sudo apt install ros-melodic-cartographer-ros```<br/>
```sudo apt install ros-melodic-move-base```

**Launching the demo**<br/>

On ROBOTONT on-board computer, launch 2d_nav_carto.launch<br/>
```roslaunch robotont_demos 2d_nav_carto.launch```

On user PC, launch display_2d_mapping.launch to visualize the result<br/>
```roslaunch robotont_demos display_2d_mapping.launch```

## AR tracking

*You only need to run these commands if this is the first time you you run this demo with the current user PC or ROBOTONT on-board computer.*

On ROBOTONT on-board computer, install ROS wrapper for alvar<br/>
```sudo apt update```
```sudo apt install ros-melodic-ar-track-alvar```

**Launching the demo**<br/>

On ROBOTONT on-board computer, launch ar_follow_the_leader.launch<br/>
```roslaunch robotont_demos ar_follow_the_leader.launch```

On user PC, launch display_ar_marker.launch to visualize the result<br/>
```roslaunch robotont_demos display_ar_marker.launch marker_id:=tag_nr```
