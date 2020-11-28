from jetbot import Robot
import time


class Maneuver:
    
    def __init__(self,myrobot):
        self.robot = myrobot
    def execute_maneuver(self):
        self.robot.set_motors(.3,.6)
        time.sleep(1.2)
        self.robot.set_motors(.7,.3)
        time.sleep(1)
        self.robot.set_motors(.5,.5)
        time.sleep(1.2)
        self.robot.set_motors(.6,.3)
        time.sleep(1)
        self.robot.set_motors(.3,.6)
        time.sleep(1.3)
        self.robot.set_motors(.5,.5)
        time.sleep(2)
        self.robot.stop()
