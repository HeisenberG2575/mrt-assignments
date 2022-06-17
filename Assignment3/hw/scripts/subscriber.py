#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import String
import numpy as np
from matplotlib import pyplot
import time
#1-forward 2-right 3-backward 4-left
def process(data):
    #print('buttons ',data.buttons)
    #print('axes ',data.axes)
    l=['FORWARD','RIGHT','BACKWARD','LEFT']
    temp=[]
    print(data.axes)
    if data.axes[0]>0.1 : 
        #print(l[i],end=' ')
        temp+=[l[3],data.axes[0]]
    elif data.axes[0]<-0.1 :
        temp+=[l[1],data.axes[0]]
    if data.axes[1]>0.1 :
        temp+=[l[0],data.axes[1]]
    elif data.axes[1]<-0.1:
        temp+=[l[2],data.axes[1]]
    #print('')
    send(temp)

def send(msg):
    rospy.loginfo(msg)
    pub.publish(' '.join(msg))

def listener():
    rospy.Subscriber("joy", Joy, process)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    pub = rospy.Publisher('joy_data', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    listener()
