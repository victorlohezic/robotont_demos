# robotont_demos
This repository is a ROS package that contains various demos showing the capabilities of the Robotont platform

## Setting up the connection between the robot and your pc
### 1. Connect your pc to Robotont's hotspot or the same network Robotont is connected to.
### 2. Configure Robotont's side of the network:
* Open a new terminal window on your pc
* Estabish an SSH connection to the robot:<br/>
```ssh username@robotont_IP_address```
* If the computer asks a "yes/no" question, type "yes"
* Enter the password: t0ndik00bas
* Set ROS_MASTER_URI: <br/>
```export ROS_MASTER_URI=http://robotont_IP_address:11311```
* Set ROS_HOSTNAME: <br/>
```export ROS_HOSTNAME=robotont_IP_address```
### 3. Configure the pc's side of the network:
* Open a new terminal window on your pc
* Set ROS_MASTER_URI: <br/>
```export ROS_MASTER_URI=http://robotont_IP_address:11311```
* Set ROS_HOSTNAME: <br/>
```export ROS_HOSTNAME=your_pc_IP_address```

## 3D mapping
### 1. Set up a connection between your pc and robotont
### 2. Install ROS wrapper of RTAB-Map:<br/>
```sudo apt-get install ros-melodic-rtabmap-ros```
### 3. Launch 3d_mapping.launch on the robotont's terminal:<br/>
```roslaunch robotont_demos 3d_mapping.launch```
### 4.To visualize the result launch display_3d_mapping.launch on the pc's terminal:<br/>
```roslaunch robotont_demos display_3d_mapping.launch```

## AR tracking
### 1. Set up a connection between your pc and robotont
### 2. Install ROS wrapper for alvar:<br/>
```sudo apt-get install ros-melodic-ar-track-alvar```
### 3. Launch ar_follow_the_leader.launch on the robotont's terminal:<br/>
```roslaunch robotont_demos ar_follow_the_leader.launch```
### 4. To visualize the marker and the robot launch display_ar_marker.launch on the pc's terminal:<br/>
```roslaunch robotont_demos display_ar_marker.launch```
