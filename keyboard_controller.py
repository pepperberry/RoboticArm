#ros 2 python client library
import rclpy 
from rclpy.node import Node 

#publish and subscribe to messages w/ floatng point numbers
from std_msgs.msg import Float64MultiArray 

from pynput import keyboard

class KeyboardController(Node):
    def __init__(self):
        super().__init__('keyboard_controller')
#creates a publisher tp publish the messages w/ queue size 10
        self.publisher_= self.create_publisher(Float64MultiArray, 'servo_commands', 10)
#initalizes the servo angle to 90 degrees
        self.angle = [90.0] * 5
#cre3ates a timer that calls timer_callback every 0.1 seconds
        self.create_timer(0.1, self.timer_callback)
#timer callback checks key and changes angle var then sends angle var message


    def timer_callback(self):
        #claw
        if keyboard.is_pressed('1'):
            self.angle[4] += 1.0
        elif keyboard.is_pressed('2'):
            self.angle[4] -= 1.0
        #wrist
        elif keyboard.is_pressed('q'):
            self.angle[3] += 1.0
        elif keyboard.is_pressed('w'):
            self.angle[3] -= 1.0
        #elbow
        elif keyboard.is_pressed('a'):
            self.angle[2] += 1.0
        elif keyboard.is_pressed('s'):
            self.angle[2] -= 1.0
        #shoulder
        elif keyboard.is_pressed('z'):
            self.angle[1] += 1.0
        elif keyboard.is_pressed('x'):
            self.angle[1] -= 1.0
        #base
        elif keyboard.is_pressed('j'):
            self.angle[0] += 1.0
        elif keyboard.is_pressed('l'):
            self.angle[0] -= 1.0
    


        #publishes message stuff
        msg = Float64MultiArray()
        msg.data = self.angles
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
