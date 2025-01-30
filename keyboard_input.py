"""
author: Pepper Berry
date: jan 30th 2025
use: this is our publisher file for simple motor movements for all 5 motos controlled by keyboard inputs
the subscriber file for this is called servo_controller
the diffrence between this and the previous files is that it uses an array and overall has more code
"""

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray

class InputControl(Node):
  def __init__(self):
    super().__init__('input_controller')
    
    #setup an inital angle to modify 
    self.angle = [245] 
    
    self.publisher_=self.create_publisher(Float64MultiArray, 'servo_command', 10)
    self.first();
    self.run();

  #passed a intial message to set the motor to our intial angle
  def first(self):
    msg = Float64MultiArray()
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
          self.angle += 1.0
        elif command == 's':
          self.angle -=1.0
        msg = Float64MultiArray()
        msg.data = self.angle
        self.publisher_.publish(msg)
        print("published")
    except KeyboardInterrupt:
      pass

def main(args=None):
  rclpy.init(args=args)
  input_control = InputControl()
  rclpy.shutdown()

if __name__ == '__main__':
  main()



