#cameraPublisher.py - > robotPublisher.py (shows image and hand tracking) -> robotSubsriber.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from std_msgs.msg import Int32
import time
import random

class ImageSubscriberNode(Node):

    def __init__(self):
        super().__init__('image_subscriber_node')

#same code between pub and sub files
        # CvBridge converts OpenCV images to ROS2 messages allows them to be sent via topics
        self.bridgeObject = CvBridge()
    
        # topic they will subsribe/publish to
        self.topicNameFrames='topic_camera_image'
 
        self.queueSize=5
    

        self.subscription = self.create_subscription(
            Image,
            self.topicNameFrames,
            self.image_callback,
            self.queueSize)
            
        self.publisher_move= self.create_publisher(Int32, 'robot_move', 10)

        # Declare variables for hand detection and game logic
        self.detector = HandDetector(detectionCon=0.3, maxHands=1)
        self.scores = [0, 0]  # [robot, player]
        self.timer = 0
        self.stateResult = False
        self.startGame = False
        self.intialTime = time.time()
        self.randomNumber = 0
        print("rock = 1, paper = 2, scissors =3")

    def image_callback(self, msg):
        # Convert ROS2 Image message to OpenCV format
        img = self.bridgeObject.imgmsg_to_cv2(msg)
        #img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_LINEAR)

        # Hand detection
        hands, img = self.detector.findHands(img)

        if self.startGame:
            if not self.stateResult:
                self.timer = time.time() - self.intialTime
                
                cv2.putText(img, str(int(self.timer)), (550, 450), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

                if self.timer > 4:
                    self.stateResult = True
                    self.timer = 0
                    time.sleep(0.25)
			
                    if hands:
                        playerMove = None
                        hand = hands[0]
                        fingers = self.detector.fingersUp(hand)

                        if fingers == [0, 0, 0, 0, 0]:
                            playerMove = 1  # Rock
                        elif fingers == [1, 1, 1, 1, 1]:
                            playerMove = 2  # Paper
                        elif fingers == [0, 1, 1, 0, 0]:
                            playerMove = 3  # Scissors

                        
                        
                        # Determine winner
                        if (playerMove == 1 and self.randomNumber == 3) or \
                           (playerMove == 2 and self.randomNumber == 1) or \
                           (playerMove == 3 and self.randomNumber == 2):
                            self.scores[1] += 1  # Player wins

                        elif (playerMove == 3 and self.randomNumber == 1) or \
                             (playerMove == 1 and self.randomNumber == 2) or \
                             (playerMove == 2 and self.randomNumber == 3):
                            self.scores[0] += 1  # Robot wins
			
			
                        print(f"Player: {playerMove}, Robot: {self.randomNumber}")

        # Display scores and timer
        cv2.putText(img, f"Robot:{self.scores[0]}", (10, 35), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 4)
        cv2.putText(img, f"Person:{self.scores[1]}", (400, 35), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 4)
        cv2.imshow("Camera video", img)

        key = cv2.waitKey(2)
        if key == ord('g'): # basically publishes that you are done, sets robot motors to zero
        	msg = Int32()
        	msg.data = 4
        	self.publisher_move.publish(msg)
        if key == ord('s'):
            self.startGame = True
            self.intialTime = time.time()
            self.stateResult = False
            #publish robots move
            self.randomNumber = random.randint(1, 3)
            msg = Int32()
            msg.data = self.randomNumber
            self.publisher_move.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    subscriber_node = ImageSubscriberNode()
    rclpy.spin(subscriber_node) #subscribing constatnly
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

