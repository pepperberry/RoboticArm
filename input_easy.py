import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

class InputControl(Node):
  def __init__(self):
    super().__init__('input_controller')
    self.publisher_=self.create_publisher(Float64, 'servo_command', 10)
    self.run();
    
  def run(self):
    msg = Float64MultiArray()
    msg.data = 40
    self.publisher.publish(msg)
    print("published")

def main(args=None):
  rclpy.init(args=args)
  input_control = InputControl()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
      
