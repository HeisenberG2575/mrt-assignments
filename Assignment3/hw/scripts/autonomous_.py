#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy
from math import floor
from math import abs

#---------------------------------------------------- 
def conv(data):
    return floor(127*abs(data)) 
class Drive:
    def __init__(self,driver1,driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2
         

    def drive_callback(self,inp):
        # A bit of help! These are arrays of data
        axes = inp.axes #inp is msg.Joy type
                        #in msg 0 index is lt/rt index 1 is for/bak
        buttons = inp.buttons

 
        if axes[0]>0.1 : 
            self.leftClaw.ForwardMixed(conv(axes[0]))
            self.rightClaw.BackwardMixed(conv(axes[0]))
        elif axes[0]<-0.1 :
            self.leftClaw.BackwardMixed(conv(axes[0]))
            self.rightClaw.ForwardMixed(conv(axes[0]))
        if axes[1]>0.1 :
            self.leftClaw.ForwardMixed(conv(axes[0]))
            self.rightClaw.ForwardMixed(conv(axes[0]))
        elif axes[1]<-0.1:
            self.leftClaw.BackwardMixed(conv(axes[0]))
            self.rightClaw.BackwardMixed(conv(axes[0]))

                

#---------------------------------------------------                



