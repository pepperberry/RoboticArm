#cameraPublisher.py - > robotPublisher.py -> robotSubsriber.py takes in number and does robo movement based on that number

import rclpy 
import time
from rclpy.node import Node 

from std_msgs.msg import Int32

import adafruit_pca9685
from adafruit_pca9685 import PCA9685
import board
import busio

class robotSubsrciber(Node):
    def __init__(self):
    	super().__init__('robot_Subsrciber')
    	self.pca = adafruit_pca9685.PCA9685(board.I2C())
    	self.pca.frequency = 50
    	#inital posiotion
    	self.pca.channels[0].duty_cycle = int((110 / 180.0) * 4096)
    	self.pca.channels[1].duty_cycle = int((150 / 100.0) * 4096)
    	self.pca.channels[2].duty_cycle = int((260 / 180.0) * 4096)
    	self.pca.channels[3].duty_cycle = int((180 / 180.0) * 4096)
    	self.pca.channels[4].duty_cycle = int((250 / 180.0) * 4096)
    	
    	
    	self.subscription = self.create_subscription(Int32, 'robot_move', self.listener_callback, 10)
    	
    def listener_callback(self, msg):
    	if msg.data == 4: # stops the motors
    		self.pca.channels[0].duty_cycle = 0
    		self.pca.channels[1].duty_cycle = 0
    		self.pca.channels[2].duty_cycle = 0
    		self.pca.channels[3].duty_cycle = 0
    		self.pca.channels[4].duty_cycle = 0
    	else:
    		#moves the robot arm up and down like you normally do playing rock-paper-scissors
	    	self.up_down()
	    	self.up_down()
	    	self.up_down()
	    	self.up_down()
	    	if msg.data == 1: # Rock
	    		self.set_servo_rock()
	    	elif msg.data == 2: # Paper
	    		self.set_servo_paper()
	    	elif msg.data == 3: #Scissors
	    		self.set_servo_scissors()
	    	time.sleep(4)
	    	self.pca.channels[0].duty_cycle = int((110 / 180.0) * 4096)
	    	self.pca.channels[1].duty_cycle = int((150 / 100.0) * 4096)
	    	self.pca.channels[2].duty_cycle = int((260 / 180.0) * 4096)
	    	self.pca.channels[3].duty_cycle = int((180 / 180.0) * 4096)
	    	self.pca.channels[4].duty_cycle = int((250 / 180.0) * 4096)
    
	# each set to move to a position similar to what rock, paper and scissors look like you can change these to make them easier to understand.    		
    def set_servo_rock(self):
    	self.pca.channels[2].duty_cycle = int((240 / 180.0) * 4096)
    	self.pca.channels[3].duty_cycle = int((350 / 180.0) * 4096)
    	self.pca.channels[4].duty_cycle = int((300 / 180.0) * 4096)
    def set_servo_paper(self):
    	self.pca.channels[2].duty_cycle = int((240 / 180.0) * 4096)
    	self.pca.channels[3].duty_cycle = int((180 / 180.0) * 4096)
    	self.pca.channels[4].duty_cycle = int((300 / 180.0) * 4096)
    def set_servo_scissors(self):
    	self.pca.channels[2].duty_cycle = int((240 / 180.0) * 4096)
    	self.pca.channels[3].duty_cycle = int((180 / 180.0) * 4096)
    	self.pca.channels[4].duty_cycle = int((40 / 180.0) * 4096)
    def up_down(self):
    	time.sleep(0.35)
    	self.pca.channels[2].duty_cycle = int((210 / 180.0) * 4096)
    	time.sleep(0.35)
    	self.pca.channels[2].duty_cycle = int((270 / 180.0) * 4096)
    	
# defines the main
def main(args=None):
    rclpy.init(args=args) #initalizes library
    node = robotSubsrciber() #creates an instance
    rclpy.spin(node) #keep running and process when it gets a message
    node.destroy_node() #destroys when done
    self.pca.channels[0].duty_cycle = 0
    self.pca.channels[1].duty_cycle = 0
    self.pca.channels[2].duty_cycle = 0
    self.pca.channels[3].duty_cycle = 0
    self.pca.channels[4].duty_cycle = 0
    rclpy.shutdown()

#entry point of script
if __name__ == '__main__':
    main()
