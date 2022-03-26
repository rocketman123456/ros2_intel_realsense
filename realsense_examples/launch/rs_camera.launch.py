# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# /* Author: Gary Liu */
import os
import launch
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    #camera_base_frame_id = LaunchConfiguration('base_frame_id', default='d435i_link')
    #camera_serial_no = LaunchConfiguration('serial_no', default='109622073740')
    camera_align_depth = LaunchConfiguration('align_depth', default=True)
    camera_color_fps = LaunchConfiguration('color0.fps', default='60')
    camera_depth_fps = LaunchConfiguration('depth0.fps', default='60')
    camera_infra1_fps = LaunchConfiguration('infra1.fps', default='60')
    camera_infra2_fps = LaunchConfiguration('infra2.fps', default='60')
    rgbd_node = Node(
        package='realsense_node',
        executable='realsense_node',
        namespace='/d435i',
        output='screen',
        parameters=[{
            'align_depth' : camera_align_depth,
            'color0.fps' : camera_color_fps,
            'depth0.fps' : camera_depth_fps,
            'infra1.fps' : camera_infra1_fps,
            'infra2.fps' : camera_infra2_fps
        }]
    )
    return launch.LaunchDescription([rgbd_node])
