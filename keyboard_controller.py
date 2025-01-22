#ros 2 python client library
import rclpy 
from rclpy.node import Node 

#publish and subscribe to messages w/ floatng point numbers
from std_msgs.msg import Float64 

import keyboard

class KeyboardController(Node):
    def __init__(self):
        super().__init__('keyboard_controller')
#creates a publisher tp publish the messages w/ queue size 10
        self.publisher_= self.create_publisher(Float64, 'servo_command', 10)
#initalizes the servo angle to 90 degrees
        self.angle = 90.0
#cre3ates a timer that calls timer_callback every 0.1 seconds
        self.create_timer(0.1, self.timer_callback)
#timer callback checks key and changes angle var then sends angle var message
    def timer_callback(self):
        if keyboard.is_pressed('Q'):
            self.angle += 1.0
        elif keyboard.is_pressed('W'):
            self.angle -= 1.0
        msg = Float64()
        msg.data = self.angle
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    node = KeyboardController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()