#cameraPublisher.py(gets and publishes image) - > robotPublisher.py -> robotSubsriber.py
import cv2 
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node 
from cv_bridge import CvBridge 
 
class PublisherNodeClass(Node):
   
    def __init__(self):

        super().__init__('publisher_node')
      
        # this is the camera device number this may vary
        self.cameraDeviceNumber=0
        
        # instance of the OpenCV VideoCapture object
        self.camera = cv2.VideoCapture(self.cameraDeviceNumber)
         
         
#same code between pub and sub files
        # CvBridge converts OpenCV images to ROS2 messages allows them to be sent via topics
        self.bridgeObject = CvBridge()
    
        # topic they will subsribe/publish to
        self.topicNameFrames='topic_camera_image'
 
        self.queueSize=5
    
#code unqiue to publisher
        # this creates the publisher that publishes to the message typed image over the topic 'self.topicNameFrames' with queue size 'self.queueSize'
        self.publisher = self.create_publisher(Image, self.topicNameFrames, self.queueSize)
      
        # publish rate
        self.periodCommunication = 0.1  
    
        # timer that calls publish function every publish rate
        self.timer = self.create_timer(self.periodCommunication, self.publish)
   
    
# this publishes when called by the timer
    def publish(self):
    	
        # here we read the frame by using the camera and resize
        success, frame = self.camera.read()
        frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_LINEAR) 
          
        # if we are able to read the frame
        if success == True:
            # convert OpenCV frame to message
            ROS2ImageMessage=self.bridgeObject.cv2_to_imgmsg(frame)
            # publish the image
            self.publisher.publish(ROS2ImageMessage)
       
 
# this is the entry point of our code
def main(args=None):
#setup
  rclpy.init(args=args)
  publisherObject = PublisherNodeClass()
# publishing 
  rclpy.spin(publisherObject) #calls recusivly for continual 'publishing'
#shutdown
  publisherObject.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
    main()
