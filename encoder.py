import serial
from jetbot import Robot 
import math
from maneuver import Maneuver
import time
#diameter in mm
WHEEL_DIAMETER = 60 
TICKS_PER_REV = 362 
WHEEL_REV = math.pi * WHEEL_DIAMETER
MM_TRAVEL_PER_TICK = WHEEL_REV / TICKS_PER_REV 

class Encoder:
    
    
    def __init__(self,goal_distance,myrobot):
        self.goal = goal_distance
        self.robot = myrobot
        
    def convertTicks_cm(self,ticks):
        distance = (int(ticks)* MM_TRAVEL_PER_TICK) / 10
        return "{:.2f}".format(distance)

    def get_data(self):
        
        #open serial port
        with serial.Serial('/dev/ttyACM0', 9600, timeout=10) as ser:
            count = 0
            while count < 1:
                count +=1 
                try:
                    
                    encoder_values = ser.readline().decode("utf-8")
                    #read data from each wheel and convert to cm 
                    encoder_values = encoder_values.replace("\r\n","")
           
                    values = encoder_values.split(":")
                    left_wheel = values[0]
                    right_wheel = values[1]
                    left_distance = float(self.convertTicks_cm(left_wheel))
                    right_distance = float(self.convertTicks_cm(right_wheel))
                    print(left_distance, " and ",right_distance)
            
                    #compare to goal distance to see if robot travel the right distance
                    if(left_distance >= self.goal or right_distance >= self.goal):
                        self.robot.stop()
                        print("Goal Reached")
                        break
            
                except IndexError:
                    print("Bad data")
