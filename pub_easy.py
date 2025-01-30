"""
author: Pepper Berry
date: jan 29th 2025
use: this is our publisher file for the simplest motor movement possible in ros2
use in conjunction with the servo_single.py our subsriber file
"""

#ros 2 python client library
import rclpy
from rclpy.node import Node

#publish and subscribe to messages w/ floatng point numbers (degrees of rotation)
from std_msgs.msg import Float32

#initalizing
class PubEasy(Node):
  def __init__(self):
    super().__init__('pub_easy')

    #creating a publisher, publishing the topic 'servo_command' this is what links our subscriber and publisher files
    self.publisher_=self.create_publisher(Float32, 'servo_command', 10)
    self.run();

  #basically just publishes 40 degrees to the topic change if needed change this
  def run(self):
    msg = Float32()
    msg.data = 245.0
    self.publisher_.publish(msg)
    print("published")

def main(args=None):
  rclpy.init(args=args)
  input_control = PubEasy()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
      
