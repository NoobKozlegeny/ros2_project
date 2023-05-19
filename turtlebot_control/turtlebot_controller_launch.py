from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot_control',
            executable='turtlebot_controller',
            name='turtlebot_controller',
            output='screen',
        ),
    ])
