
# The Steps for the Robotic Arm

### Info

Materials:

- Raspberry Pi 5
- PCA9685
- Wires and an external power supply (ask Gary for the specific name)
- heat sink provided to you
- Mouse, keyboard, monitor, and their respective power cords
- Robotic arm: Lynxmotion SES-V1 AL5D Arm

The arm uses:

- 1 x HS-485HB in the base
- 1 x HS-805BB in the shoulder
- 1 x HS-755HB in the elbow
- 1 x HS-645MG in the wrist
- 1 x HS-422 in the gripper

Objectives:

1. Learn how to set up the Raspberry Pi with Linux Ubuntu and ROS2 Jazzy.
2. Learn how to modify the physical setup of the robotic arm to function with ROS2.
3. Learn how to code a simple robot arm program and download the Adafruit libraries.
4. Create your first ROS2 package.
5. Code in ROS2.

## Objective 1: Set Up the Raspberry Pi with Linux Ubuntu and ROS2 Jazzy

**Prepare Your Materials:** 

1. Get your:
    * Micro SD card
    * USB to SD card reader.
2. Download the Raspberry Pi Imager from [Raspberry Pi Software](https://www.raspberrypi.com/software/) from your personal computer. Make sure to choose the version based on your personal computer's operating system (Windows, Mac, or Linux).

**Install the Operating System:**  

1. Install the Raspberry PI imager on your personal computer. Make sure your card reader is connected to your personal computer.
1. Once the software has finished installing, select `Raspberry Pi 5` as the hardware.  
1. Select `General-purpose OS` then select `Ubuntu 24.04.1 LTS`.  
1. Select the SD card you are using as the storage device.  
1. Once the installation is complete, remove the SD card from the card reader.

**Connect the Necessary Components:**  

Connect the following: 

* Power supply: Use a 27W USB-C cable for the power supply. 
* Insert the micro SD card: The micro SD card slot is on the bottom of the Raspberry Pi.
* Display cord: Connect the Raspberry Pi to a monitor. Use HDMI port 0 and a suitable cord for your monitor.
* Keyboard/mouse cords: for the keyboard and mouse, we will use a tiny touchpad keyboard, but you can use any mouse and keyboard combo. Plug it into the USB port on the Raspberry Pi. 

**Boot Up the Raspberry Pi:**  

Once it boots up, it will prompt you to set your language and time zone. Make sure to choose them correctly.  
Next, it will ask you to create a desktop name, username, and password. Make sure the username is "test" (other details can be your choice). Remember your password.  
Select your Wi-Fi network, as you will need Wi-Fi later.  

**Update the System:**  

Open the terminal and type in the following commands one at a time, pressing Enter after each command:  

```bash
sudo apt update  
sudo apt upgrade 
sudo apt install git
```

**Download ROS2:**  

Once Ubuntu is set up, download ROS2 using scripts from GitHub by entering the following commands in the terminal one at a time, pressing Enter after each command:  
```bash
git clone https://github.com/SU-Innovation-Lab/ROS2`  
cd ROS2  
cd config  
chmod +x setup.sh  
./setup.sh
```
These commands will fully install ROS2. don't worry it will restart.


**Reference Videos (Optional):**  
[Install Linux Ubuntu](https://www.youtube.com/watch?v=dAazTc2xuMw&ab_channel=AleksandarHaberPhD)   
[Install ROS2 Jazzy](https://www.youtube.com/watch?v=Vl9tkUv7Y7o&ab_channel=AleksandarHaberPhD)

## Objective 2: Learn How to Change the Physical Setup of the Robotic Arm to Function with ROS2

**Remove the SSC-32U Board:**  

When you receive the robotic arm, it will come with a PCB board labeled SSC-32U.  
To remove the board, start by unscrewing the back base plate to which the board and its switch are attached.  
Once the board is removed, put the screws back into the robot for added stability.  

**Attach the PCA9685 Board:**  

Connect the wires to the PCA9685 board in the following order:  
 * Inside: pulse/PWM  
 * Middle: VS1/V+  
 * Outside: GND  

Ensure the same order is followed for each row (row 0 to row 0, etc.).  

**Connect the Board to the Power Supply:**  

Two wires will screw into the green box on the board.    
The other two wires will connect to the power supply.    
Make sure to connect the positive (+) to the positive (+) and the negative (-) to the negative (-).    

**Prepare the Raspberry Pi 5:**  

Attach the heat sink, which is usually a piece of metal with grooves to conduct airflow.  
If you have tiny grey squares, place them on the raised parts of the bottom of the cooling piece so that they touch the parts once screwed on.  
Make sure to remove the plastic pieces from both sides before screwing the heat sink together.  

**Connecting the board to the PI:**  
![setup of board connecting the wires from PCA9685 board to the pi](https://cdn-learn.adafruit.com/assets/assets/000/069/564/original/components_raspi_pca9685_i2c_with_servo.jpg?1547757668)
here is the setup just connect the wires as shown in the image.

## Objective 3: Learn How to Code a Simple Robot Arm Program and Download the Adafruit Libraries  

Now that ROS2 is set up, we will set up the robot arm and PCA9685 board.  

**Install Necessary Packages:**  

Open the terminal and enter the following commands. Press Enter between each line's command:
```bash
sudo apt-get install python3-smbus  
sudo apt-get install i2c-tools 
```
**Check Connection:**   

Make sure the PCA9685 is connected and enter the following terminal command, then press Enter:  
```bash
sudo i2cdetect -y 1
```
 
If the board is properly connected, it will output the connection details.  

![output of sudo i2cdetect -y 1](https://cdn-learn.adafruit.com/assets/assets/000/001/700/original/raspberry_pi_i2cdetect.png?1396775470)

**Install Necessary Libraries:**  

Type the following commands into the command line, pressing Enter after each line: 
```bash
sudo apt-get install python3 python3-pip  
pip install RPi.GPIO 
pip install Adafruit-Blinka
pip install adafruit-circuitpython-servokit
```

**Write Your First Python Program:**  

Create a folder to put your code in. Use the following command:  
```bash
mkdir robot_arm_code
cd robot_arm_code
```

Create and open a new file with the following command:
```bash
nano robotFirstTest.py
```

Once the new file is open, add the following code:  
```python
from adafruit_servokit import ServoKit  
kit = ServoKit(channels=16)
kit.servo[0].angle = 180
```

This moves the motor on channel 0 to 180 degrees. Ensure that this won't cause the robot to bump into anything and that there is a motor in that spot.  
To save and exit, press <kbd>Ctrl</kbd> + <kbd>o</kbd>, then <kbd>Ctrl</kbd> + <kbd>x</kbd> .  

To run the code, type the following command, then press Enter:  
```bash
python3 robotFirstTest.py
``` 

**Testing and Notes:**  

At this point, you can code some simple movements using this code. It is advisable to write down which ports go to which motors to ensure proper movements. Also, test which way each motor moves to  determine if 0 degrees is up or down.  

## Objective 4: Createing your first ROS2 package.

Source your setup and create your ros2 work station  
```bash
source /opt/ros/jazzy/setup.bash
cd ~
mkdir -p ros2_ws/src
cd ~/ros2_ws
```
next build the package and create it
```bash
colcon build
source install/setup.bash
cd src
ros2 pkg create --build-type ament_python package
cd package
```
replace `package` with the name of your package, I named mine RoboArm but you can choose what you would like.  
you can make multiple packages but all of them should be included in your src folder.

**file setup**
next let's make sure our files are setup properly, use `ls` to find what files and folders are in your package and `nano` to open:
* `package.xml` & `setup.py`: make sure to update the package description, license, and maintiner email.



## Objective 5: Codeing simple programs in ROS2.

**Additional Information and Key Concepts**  

To go more in depth or for information beyond the scope of this project, you can refer to the [ROS2 Jazzy Documentation](https://docs.ros.org/en/jazzy/Tutorials.html). It contains a lot of tutorials, ranging in difficulty, depending on what you want to achieve. You don’t need to look at this to understand the project.  
For this ROS project, we use the basics: nodes, a topic, a publisher, and a subscriber.  

- Nodes  

Nodes perform individual tasks. For example, in a very complex robot, you might have one node for the camera, one for driving, and one for the arms.  
In this project, we have two nodes: the Publisher node and the Subscriber node. Each node can publish and subscribe to multiple topics, but to keep it simple, we are having one node for each.  

- Publisher and Subscriber
  
In the example code, each file has ‘pub’ if it is a publisher and ‘sub’ if it is a subscriber.  
The publisher node puts out information.  
The subscriber node receives this information. It's like playing a game of telephone.  

- Topics
  
How does the subscriber node know what to ‘listen’ to? It listens for a particular topic. When the publisher node initializes, it names the topic it is publishing to. In our code, it's called ‘servo_command’.  

Now that we understand these basic concepts, let's delve into the key parts of ROS2 code for this project.

**Imports:**  
```python
#ros 2 python client library
import rclpy 
from rclpy.node import Node

#publish and subscribe to messages w/ floatng point numbers (degrees of rotation)
from std_msgs.msg import Float32

#imports the pca9865 board libraries to interact with it
import adafruit_pca9685
from adafruit_pca9685 import PCA9685
import board
import busio`
```

Both files need the ROS2 Python client library to be imported, as both use ROS2 functionality (publishers and subscribers). Additionally, they need to import the same type of message so the subscriber can understand the message sent by the publisher. Only the subscriber needs the Adafruit libraries, as only the subscriber works with the Adafruit board.

**Subscriber & publisher:**

```python
self.subscription = self.create_subscription(Float32, 'servo_command', self.listener_callback, 10)

self.publisher_=self.create_publisher(Float32, 'servo_command', 10)
```

Each file needs a statement to initialize their subscriber/publisher. Both have the same fundamental parts in the parentheses. `Float32` is our message variable type which we imported above. `servo_command` is our topic. `10` is the size of our message queue. All three of these things need to be consistent across the publisher and subscriber.

`self.listener_callback` is what happens after we get the message data and can have any name as long as it is connected to the defined function.

```python
 def listener_callback(self, msg):
     
     #lets us know what the single servo is
     channel = 0
     
     print("got message")
     self.set_servo_angle(channel, msg.data)
```

This function can then perform any desired action with the data. In this simple case, it sets a servo in channel `0` to the degree specified in the message.

**Publishing a message:**  
```python
msg = Float32()
msg.data = 245.0
self.publisher_.publish(msg)
```
For each message, you need to initialize it as the type of message. If you want to know all the types of messages you can send and their syntax, refer to the [ROS2 Message Documentation](https://docs.ros.org/en/melodic/api/std_msgs/html/index-msg.html). Then, specify what data the message holds and finally publish the message.  
Each call to a message creates a new message. The only job of a message is to hold and publish data.

**Diagram:**    
Here is a commonly used diagram to describe how nodes are connected by topics and how messages are published and received: [Understanding ROS2 Nodes](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

**Pre-Written Code:**  
The GitHub contains four sets of code, each working through a specific part of writing code in ROS2. In the end, you will have code that can move all five motors using keyboard commands, similar to how you would move around in a video game. Moving forward, we can use this code and sensors to create more complex movements, including using OpenAI along with a camera to identify particular things, like playing rock-paper-scissors.

1st Set:  
This is the bare-bones code for moving one motor (currently set to motor `0`) to a hard-coded position.

* Publisher: `pub_easy.py`  
* Subscriber: `sub_easy.py`  

2nd Set:  
This is the 1st set, but you can input commands to move the robot left or right, still only moving one motor.

* Publisher: `pub_simple_input.py`  
* Subscriber: `sub_easy.py`  

3rd Set:  
This set has the same operational abilities as the 2nd set, except it controls all five motors.

* Publisher: `pub_multi_input.py`  
* Subscriber: `sub_multi_motor.py`  

4th Set:  
This set has the same abilities as the 3rd set but has a better user interface for using the robot arm. (not finished yet)

* Publisher: `keyboard_controller.py`  
* Subscriber: `sub_multi_motor.py`

**running the code**

navigate to `setup.py` and update the `console_scripts` to include the files you are going to use in the format:*check this is true  
```python
file1 = package.file1:main
file2 = package.file2:main
```
once you have code written make sure to do these three steps, later we can simplify this using a launch file but right now we will do this so we can debug files individually
```bash
cd ~/ros2_ws
source ~/ros2_ws/install/setup.bash
ros2 run package file.py
```
replace the `package` with your package name and `file.py` with the name of your file you will need a terminal window open for each file you are running and to do these steps in each window.
