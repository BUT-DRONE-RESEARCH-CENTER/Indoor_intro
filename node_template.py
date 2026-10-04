#!/usr/bin/env python3

import csv
import rclpy
from rclpy.node import Node

# Message import
from geometry_msgs.msg import TransformStamped, PoseStamped
from nav_msgs.msg import Path


class PoseCsvLogger(Node):

    def __init__(self):
        super().__init__('pose_csv_logger')

        # 1. CSV file setup
        self.filename = 'robot_trajectory.csv'
        self.csv_file = open(self.filename, mode='w', newline='')
        self.writer = csv.writer(self.csv_file)

        # TODO: Write CSV header based on what you will be saving
        # self.writer.writerow([])

        # Variables
        self.latest_msg = None
        self.path_msg = Path()  # Path object for Rviz trajectory

        # 2. Subscriber
        # TODO: Uncomment and fill out MESSAGE_TYPE and the right TOPIC_NAME based on the rosbag
        # self.subscription = self.create_subscription(
        #     MESSAGE_TYPE,
        #     '/TOPIC_NAME',
        #     self.pose_callback,
        #     10
        # )

        # Publishers RViz2 (Ready for trajectory visualization)
        self.pose_pub = self.create_publisher(PoseStamped, '/drone/pose', 10)
        self.path_pub = self.create_publisher(Path, '/drone/path', 10)

        # 4. Creation of data saving 10 Hz timer
        # TODO: create timer a setup it's callback
        # self.timer = 

        self.get_logger().info(
            "Node 'pose_csv_logger' is up and running..."
        )

    def pose_callback(self, msg: TransformStamped):
        self.latest_msg = msg

        # --- TransformStamped to PoseStamped mapping for RViz ---
        pose_stamped = PoseStamped()
        
        # Timestamp from the bag, frame_id set on 'world'
        pose_stamped.header.stamp = msg.header.stamp
        pose_stamped.header.frame_id = 'world'

        pose_stamped.pose.position.x = msg.transform.translation.x
        pose_stamped.pose.position.y = msg.transform.translation.y
        pose_stamped.pose.position.z = msg.transform.translation.z
        
        pose_stamped.pose.orientation = msg.transform.rotation

        # Publish actual pose
        self.pose_pub.publish(pose_stamped)

        # Add to trajectory and publish it
        self.path_msg.header.stamp = msg.header.stamp
        self.path_msg.header.frame_id = 'world'
        self.path_msg.poses.append(pose_stamped)
        self.path_pub.publish(self.path_msg)

    def timer_callback(self):
        """Called 10x per second (10 Hz)"""
        # Wait for first message 
        if self.latest_msg is None:
            return

        # TODO: Extract values from self.latest_msg (Time stamp a position X, Y, Z)
        # timestamp = ...
        # x = ...
        # y = ...
        # z = ...

        # TODO: Write extracted data to CSV file
 
        self.csv_file.flush() # Write CSV file to disk

    def destroy_node(self):
        """Correct exit for keyboard interrupts (Ctrl+C)"""
        if hasattr(self, 'csv_file') and not self.csv_file.closed:
            self.csv_file.close()
            self.get_logger().info(
                f'Data was saved successfully to {self.filename}'
            )
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = PoseCsvLogger()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
