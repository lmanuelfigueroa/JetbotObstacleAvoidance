# OverView

This project was part of my undergrad Capstone Project at CSUCI. The goal of the robot was to implement machine learning to detect and avoid obstacles and to utilize  encoders to precisely get the distance the robot has travel to use for go to goal functionality. The robot is an easy to assemble SparkFun JetBot AI Kit v2.1. It uses a Jetson Nano to process the images on the camera to detect object and nativate around them. It uses an Arduino Uno to receive the ticks from the encoders to compute the distance the robot has traveled.  

## Experience Gained 
* Python 
* Arduino C++ 
* Microntrollers 

1. Interrupts 
2. Digital Inputs and Outputs 
* Jetson Nano
1. I2C Bus
2. Serial Communication between Arduino and Jetson Nano
3. Linux 
4. JupiderHub 

## Program and Code requisites 
* Python 3 
* Arduno IDE 

## HardWare Requisites
* SparkFun JetBot AI Kit V2.0(Contains Jetson Nano but no wheel encoders)
* 2 Wheel SparkFun Encoders 
* Arduino Uno 
* 6 male to male wire jumper cables for Arduino 
* USB Data Sync Cable for Arduino U

## Getting Started
* Install Python 3 in Jetson Nano
* Install Arduino IDE in Jetson Nano or another computer 
* Set up JupyterHub account 
[Github page for Jetbot examples](https://github.com/NVIDIA-AI-IOT/jetbot/wiki/examples)
## Assembly
[Link to Assembly Guide for Jetbot](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20?_ga=2.261292105.536387234.1606373246-1000841287.1602133051)

## Code
* Arduino (C++)
"encoder_program.py" contains the program that reads the ticks from the encoders and displays them in the serial monitor. This output will be received through serial communication to Jetson Nano as bytes and the Jetson Nano will process the data and determine the distance the robot has traveled.

* Python 
3 JupyderHub files for collecting data for training, training and testing the obstacle detection 

