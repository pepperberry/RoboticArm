import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

class InputEasy(Node):
  def __init__(self):
    super().__init__('input_easy')
    self.publisher_=self.create_publisher(Float64, 'servo_command', 10)
    self.run();
    
  def run(self):
    msg = Float64()
    msg.data = 40
    self.publisher_.publish(msg)
    print("published")

def main(args=None):
  rclpy.init(args=args)
  input_control = InputEasy()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
      
