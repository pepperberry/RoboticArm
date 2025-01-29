#ros 2 python client library
import rclpy 
from rclpy.node import Node 

#publish and subscribe to messages w/ floatng point numbers
from std_msgs.msg import Float64MultiArray

#imports the pca9865 board libraries to interact with it
from adafruit_pca9685 import PCA9685
import board
import busio

#initalizing 
class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
#declaring parameters, should be set from launch files
        self.declare_parameters(
            namespace='',
            parameters=[
                ('servo_channels', [0, 1, 2, 3, 4]),
                ('frequency', 50),
                ('min_pulse', 1000),
                ('max_pulse', 2000)
            ]
        )
#retrieves values and stores them
        self.servo_channel = self.get_parameter('servo_channels').get_parameter_value().integer_array_value
        self.frequency = self.get_parameter('frequency').get_parameter_value().integer_value
        self.min_pulse = self.get_parameter('min_pulse').get_parameter_value().integer_value
        self.max_pulse = self.get_parameter('max_pulse').get_parameter_value().integer_value
#sets up 12c communication with the board
        i2c = busio.I2C(board.SCL, board.SDA)
        self.pwm = PCA9685(i2c)
        self.pwm.frequency = self.frequency
#subsrcirbes to the servo command topic and calls listner_callback when message heard
        self.subscription = self.create_subscription(
            Float64MultiArray,
            'servo_commands',
            self.listner_callback,
            10)
        self.subscription
#defines the listner callback method which process incoming messahes converting an angle into a pulse wicth ect...
    def listener_callback(self, msg):
        print("got message")
        for i, angle in enumerate(msg.data):
                if i < len(self.servo_channel):
                        pulse_width = self.min_pulse + (self.max_pulse - self.min_pulse) * (angle /180.0)
                        pulse_length = int(pulse_width / 1000000 * self.frequency * 4096)
                        self.pwm.channels[self.servo_channels[i]].duty_cycle = pulse_length

# defines the main
def main(args=None):
    rclpy.init(args=args) #initalizes library
    node = ServoController() #creates an instance
    rclpy.spin(node) #keep running and process callbacks
    node.destroy_node() #destroys when done
    rclpy.shutdown()

#entry point of script
if __name__ == '__main__':
    main()
