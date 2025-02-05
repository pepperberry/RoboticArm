
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

### Objective 1 Learn How to Set Up the Raspberry Pi with Linux Ubuntu and ROS2 Jazzy

#### Prepare Your Materials:

Grab your micro SD card and a USB to SD card reader.
Download the Raspberry Pi Imager from [Raspberry Pi Software](https://www.raspberrypi.com/software/) onto your computer and choose the version based on your computer's operating system (Windows, Mac, or Linux).

#### Install the Operating System:

Once the software has finished installing, select "Raspberry Pi 5" as the hardware.  
First, select "General-purpose OS," then click "Ubuntu 24.04.1 LTS."  
Select the SD card you are using as the storage device.  
Once the installation is complete, remove the SD card and insert it into the Raspberry Pi.

#### Connect the Necessary Components:

Connect the power supply, micro SD card, display cord, and keyboard/mouse.  
The micro SD card slot is on the bottom of the Raspberry Pi.  
Use a 27W USB-C cable for the power supply.  
For the keyboard and mouse, we will use a tiny touchpad keyboard, but you can use any mouse and keyboard combo. Plug it into the USB port on the Raspberry Pi.  
Connect the Raspberry Pi to a monitor. Use HDMI port 0 and a suitable cord for your monitor.

#### Boot Up the Raspberry Pi:

Once it boots up, it will prompt you to set your language and time zone make sure to choose them correctly.  
Next, it will ask you to create a desktop name, username, and password. Make sure the username is "test" (other details can be your choice). Remember your password.  
Select your Wi-Fi network, as you will need Wi-Fi later.  

#### Update the System:

Open the terminal and type in the following commands one at a time, pressing Enter after each command:  
'sudo apt update'  
'sudo apt upgrade'  
'sudo apt install git'  

#### Download ROS2:
Once Ubuntu is set up, download ROS2 using scripts from GitHub by entering the following commands in the terminal one at a time, pressing Enter after each command:  
'git clone https://github.com/SU-Innovation-Lab/ROS2'  
'cd ROS2'  
'cd config'  
'chmod +x setup.sh'  
'./setup.sh'  
These commands will fully install ROS2.  

####Reference Videos (Optional):  
[Install Linux Ubuntu](https://www.youtube.com/watch?v=dAazTc2xuMw&ab_channel=AleksandarHaberPhD) 
[Install ROS2 Jazzy](https://www.youtube.com/watch?v=Vl9tkUv7Y7o&ab_channel=AleksandarHaberPhD)

### Objective 2: Learn How to Change the Physical Setup of the Robotic Arm to Function with ROS2

#### Remove the SSC-32U Board:  
When you receive the robotic arm, it will come with a PCB board labeled SSC-32U.  
To remove the board, start by unscrewing the back base plate to which the board and its switch are attached.  
Once the board is removed, put the screws back into the robot for added stability.  

#### Attach the PCA9685 Board:  
Connect the wires to the PCA9685 board in the following order:  
  Inside: pulse/PWM  
  Middle: VS1/V+  
  Outside: GND  
Ensure the same order is followed for each row (row 0 to row 0, etc.).  

#### Connect the Board to the Power Supply:  
Two wires will screw into the green box on the board.    
The other two wires will connect to the power supply.    
Make sure to connect the positive (+) to the positive (+) and the negative (-) to the negative (-).    

#### Prepare the Raspberry Pi 5:  
Attach the heat sink, which is usually a piece of metal with grooves to conduct airflow.  
If you have tiny grey squares, place them on the raised parts of the bottom of the cooling piece so that they touch the parts once screwed on.  
Make sure to remove the plastic pieces from both sides before screwing the heat sink together.  

