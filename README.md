# Indoor Environment Monitoring using GrandSLAM

## Description
This project simulates an autonomous robot using ROS2 that performs indoor mapping and monitors environmental conditions like temperature and gas.

## Features
- SLAM-based mapping
- Autonomous navigation
- Zone classification (Room, Hall, Kitchen)
- Temperature monitoring
- Gas leak detection

## Tools Used
- ROS2
- Gazebo
- RViz
- Python

## How to Run

cd ~/env_monitor_ws
colcon build
source install/setup.bash


Run nodes:
ros2 run env_monitor_pkg monitor
ros2 run env_monitor_pkg patrol
ros2 run env_monitor_pkg zone_visualizer


## Output
- Map generation in RViz
- Robot movement in simulation
- Terminal output showing temperature and gas alerts

## GitHub
https://github.com/shakthivel406/env_monitor_project
