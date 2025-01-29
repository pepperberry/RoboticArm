#this is our publisher file

#ros 2 python client library
import rclpy
from rclpy.node import Node

#publish and subscribe to messages w/ floatng point numbers (degrees of rotation)
from std_msgs.msg import Float64

#initilzing
class InputControl(Node):
  def __init__(self):
    super().__init__('input_controller')
    self.angle = 90.0
    self.publisher_=self.create_publisher(Float64, 'servo_command', 10)
    self.run();

  #the code for entering commands
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
        self.publisher.publish(msg)
        print("published")
    except KeyboardInterrupt:
      pass

def main(args=None):
  rclpy.init(args=args)
  input_control = InputControl()
  rclpy.shutdown()

if __name__ == '__main__':
  main()



