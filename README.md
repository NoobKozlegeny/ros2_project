# Setup the environment
First we need to start the gazebo system which step to step guide is located here:
https://ros2-industrial-workshop.readthedocs.io/en/latest/_source/navigation/ROS2-Turtlebot.html

It's highly advised to leave the DOMAIN_ID on the default 0 value.

# Using the package
First we need start the gazebo 3D environment
```
ros2 launch turtlebot3_gazebo <insert world here>
```

Go into your workspace src path where hopefully you downloaded the package into, and run the script which will start the model you specified.
```
cd ~/<insert workspace here>/src
ros2 run turtlebot_control turtlebot_controller
```

The program won't stop after stopping the script. For this scenario this command should be run.
```
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.0}, angular: {z: 0.0}}'
```