# pepper berry
# publishes movement to robot via camera info
​
import cv2 
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node 
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

class PublisherNodeClass(Node):
   
    def __init__(self):
      super().__init__('publisher_node')
      
      #declare variable for the game
      self.detector = HandDetector(detectionCon=0.3, maxHands=1)
      self.scores = [0,0] # [robot, Player]
      self.timer  = 0
      self.stateResult = False
      self.startGame = False
      
      # this is the camera device number this may vary
      self.cameraDeviceNumber=0
      
      # instance of the OpenCV VideoCapture object
      self.camera = cv2.VideoCapture(self.cameraDeviceNumber)
      
      # here we read the frame by using the camera and resize
      success, img = self.camera.read()
      img = cv2.resize(img, (640,480), interpolation=cv2.INTER_LINEAR) 
      # if we are able to read the frame
      if success == True:
      # hand detection starts
            hands, img = self.detector.findHands(img) # this line makes the camera slower
            if self.startGame:
                  if self.stateResult is False:
                        self.timer = time.time() - self.intialTime
                        cv2.putText(img,str(int(self.timer)),(550,450),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
                        if self.timer>3:
                              self.stateResult = True
                              self.timer = 0
                              if hands:
                                    playerMove = None
                                    hand = hands[0]
                                    fingers = self.detector.fingersUp(hand)
                                    if fingers ==[0,0,0,0,0]:
                                          playerMove = 1 #rock
                                    if fingers ==[1,1,1,1,1]:
                                          playerMove = 2 #paper
                                    if fingers ==[0,1,1,0,0]:
                                          playerMove = 3 #scissors
                                    randomNumber = random.randint(1,3)
                                    #publish random number
                                    #player Wins
                                    if (playerMove == 1 and randomNumber == 3) or (playerMove == 2 and randomNumber == 1) or (playerMove == 3 and randomNumber == 2):
                                          self.scores[1] +=1
                                    #robot Wins
                                    if (playerMove == 3 and randomNumber == 1) or (playerMove == 1 and randomNumber == 2) or  (playerMove == 2 and randomNumber == 3):
                                          self.scores[0] +=1
                                    print("player" + str(playerMove) + ", " + "Robot" + str(randomNumber))
            # end of hand detection
            # Show the image + scores + timer on the screen
            cv2.putText(img,str("Robot:" + str(self.scores[0])),(10,35),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),4)
            cv2.putText(img,str("Person:" + str(self.scores[1])),(410,35),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),4)
            cv2.imshow("Camera video", img)
            #starts the game
            key = cv2.waitKey(2)
            if key == ord('s'):
                  self.startGame = True
                  self.intialTime = time.time()
                  self.stateResult = False
      # def publish(self):
      
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
