#ros 2 python client library
import rclpy 
from rclpy.node import Node 

#publish and subscribe to messages w/ floatng point numbers (degrees of rotation)
from std_msgs.msg import Float64

#imports the pca9865 board libraries to interact with it
import adafruit_pca9685
from adafruit_pca9685 import PCA9685
import board
import busio

#initalizing 
class ServoSingle(Node):
    def __init__(self):
        super().__init__('servo_single')
        #initalizing the board and its fequency
        self.pca = adafruit_pca9685.PCA9685(board.I2C())
        self.pca.frequency = 50

        #creating a subscription to the outputted message to the topic 'servo_command' this is the common factor between the two files
        self.subscription = self.create_subscription(Float64, 'servo_command', self.listener_callback, 10)
        #self.subscription
        
        
#defines the listner callback method which process incoming messages
    def listener_callback(self, msg):
        
        #lets us know what the single servo is
        int channel = 0;
        
        print("got message")
        self.set_servo_angle(channel, msg.data)
        
#setting the exact movemnt
    def set_servo_angle(self, channel, angle):
        pulse_length = int((angle / 180.0) * 4096)
        self.pca.channels[channel].duty_cycle = pulse_length

# defines the main
def main(args=None):
    rclpy.init(args=args) #initalizes library
    node = ServoSingle() #creates an instance
    rclpy.spin(node) #keep running and process when it gets a message
    node.destroy_node() #destroys when done
    rclpy.shutdown()

#entry point of script
if __name__ == '__main__':
    main()
