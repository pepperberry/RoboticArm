"""
author: Pepper Berry
date: jan 29th 2025
use: this is our publisher file for the simplest motor movement possible in ros2 
with actual inputs!!! comments in this file will only be about the changes between this file and pub_easy.py
use in conjunction with the sub_easy.py our subsriber file
use command 'a' for pos direction and 's' for neg direction
"""

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

class PubSimpleInput(Node):
  def __init__(self):
    super().__init__('pub_simple_input')
    
    #setup an inital angle to modify 
    self.angle = 245.0
    
    self.publisher_=self.create_publisher(Float32, 'servo_command', 10)
    self.first();
    self.run();

  #passed a intial message to set the motor to our intial angle
  def first(self):
    msg = Float32()
    msg.data = self.angle
    self.publisher_.publish(msg)
    print("published inital")

   #input how you want it to move changes the inital angle then publishes it
  def run(self):
    try:
      while rclpy.ok():
        command = input("enter command: ")
        print("captuerd command")
        if command == 'a':
          self.angle += 10.0
        elif command == 's':
          self.angle -=10.0
        msg = Float32()
        msg.data = self.angle
        self.publisher_.publish(msg)
        print("published: " + str(self.angle))
    except KeyboardInterrupt:
      pass

def main(args=None):
  rclpy.init(args=args)
  input_control = PubSimpleInput()
  rclpy.shutdown()

if __name__ == '__main__':
  main()



