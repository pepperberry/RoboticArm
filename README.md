
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

## Objective 1 Learn How to Set Up the Raspberry Pi with Linux Ubuntu and ROS2 Jazzy

**Prepare Your Materials:** 

Grab your micro SD card and a USB to SD card reader.
Download the Raspberry Pi Imager from [Raspberry Pi Software](https://www.raspberrypi.com/software/) onto your computer and choose the version based on your computer's operating system (Windows, Mac, or Linux).

**Install the Operating System:**  

Once the software has finished installing, select "Raspberry Pi 5" as the hardware.  
First, select "General-purpose OS," then click "Ubuntu 24.04.1 LTS."  
Select the SD card you are using as the storage device.  
Once the installation is complete, remove the SD card and insert it into the Raspberry Pi.

**Connect the Necessary Components:**  

Connect the power supply, micro SD card, display cord, and keyboard/mouse.  
The micro SD card slot is on the bottom of the Raspberry Pi.  
Use a 27W USB-C cable for the power supply.  
For the keyboard and mouse, we will use a tiny touchpad keyboard, but you can use any mouse and keyboard combo. Plug it into the USB port on the Raspberry Pi.  
Connect the Raspberry Pi to a monitor. Use HDMI port 0 and a suitable cord for your monitor.

**Boot Up the Raspberry Pi:**  

Once it boots up, it will prompt you to set your language and time zone make sure to choose them correctly.  
Next, it will ask you to create a desktop name, username, and password. Make sure the username is "test" (other details can be your choice). Remember your password.  
Select your Wi-Fi network, as you will need Wi-Fi later.  

**Update the System:**  

Open the terminal and type in the following commands one at a time, pressing Enter after each command:  
`sudo apt update`   
`sudo apt upgrade`  
`sudo apt install git`  

**Download ROS2:**  

Once Ubuntu is set up, download ROS2 using scripts from GitHub by entering the following commands in the terminal one at a time, pressing Enter after each command:  
`git clone https://github.com/SU-Innovation-Lab/ROS2`  
`cd ROS2`  
`cd config`  
`chmod +x setup.sh`  
`./setup.sh`  
These commands will fully install ROS2.  

####Reference Videos (Optional):  
[Install Linux Ubuntu](https://www.youtube.com/watch?v=dAazTc2xuMw&ab_channel=AleksandarHaberPhD) 
[Install ROS2 Jazzy](https://www.youtube.com/watch?v=Vl9tkUv7Y7o&ab_channel=AleksandarHaberPhD)

## Objective 2: Learn How to Change the Physical Setup of the Robotic Arm to Function with ROS2

**Remove the SSC-32U Board:**  

When you receive the robotic arm, it will come with a PCB board labeled SSC-32U.  
To remove the board, start by unscrewing the back base plate to which the board and its switch are attached.  
Once the board is removed, put the screws back into the robot for added stability.  

**Attach the PCA9685 Board:**  

Connect the wires to the PCA9685 board in the following order:  
  Inside: pulse/PWM  
  Middle: VS1/V+  
  Outside: GND  
Ensure the same order is followed for each row (row 0 to row 0, etc.).  

**Connect the Board to the Power Supply:**  

Two wires will screw into the green box on the board.    
The other two wires will connect to the power supply.    
Make sure to connect the positive (+) to the positive (+) and the negative (-) to the negative (-).    

**Prepare the Raspberry Pi 5:**  

Attach the heat sink, which is usually a piece of metal with grooves to conduct airflow.  
If you have tiny grey squares, place them on the raised parts of the bottom of the cooling piece so that they touch the parts once screwed on.  
Make sure to remove the plastic pieces from both sides before screwing the heat sink together.  

## Objective 3: Learn How to Code a Simple Robot Arm Program and Download the Adafruit Libraries  

Now that ROS2 is set up, we will set up the robot arm and PCA9685 board.  

**Install Necessary Packages: **  

Open the terminal and enter the following commands. Press Enter between each line's command:  
`sudo apt-get install python3-smbus`  
`sudo apt-get install i2c-tools`  

*Check Connection:*    

Make sure the PCA9685 is connected and enter the following terminal command, then press Enter:  
`sudo i2cdetect -y 1`  
If the board is properly connected, it will output the connection details.  

# there should be an image here

**Install Necessary Libraries:**  

Type the following commands into the command line, pressing Enter after each line:  
`sudo apt-get install python3 python3-pip`  
`pip install RPi.GPIO`  
`pip install Adafruit-Blinka`  
`pip install adafruit-circuitpython-servokit`  

**Write Your First Python Program:**  

Create a folder to put your code in. Use the following command:  
`mkdir robot_arm_code`
`cd robot_arm_code`

Create and open a new file with the following command:
`nano robotFirstTest.py`

Once the new file is open, add the following code:  
`from adafruit_servokit import ServoKit`  
`kit = ServoKit(channels=16)`  
`kit.servo[0].angle = 180`    
This moves the motor on channel 0 to 180 degrees. Ensure that this won't cause the robot to bump into anything and that there is a motor in that spot.  
To save and exit, press Control O, then Control X.  

To run the code, type the following command, then press Enter:  
`python3 robotFirstTest.py`  

**Testing and Notes:**  

At this point, you can code some simple movements using this code. It is advisable to write down which ports go to which motors to ensure proper movements. Also, test which way each motor moves to  determine if 0 degrees is up or down.  

## Objective 5

**Additional Information and Key Concepts**  

To go more in depth or for information beyond the scope of this project, you can refer to the ROS2 Jazzy Documentation. It contains a lot of tutorials, ranging in difficulty, depending on what you want to achieve. You don’t need to look at this to understand the project.  
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

