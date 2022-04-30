#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge
from matplotlib import pyplot
import time

def process(data):
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
    canny=cv2.Canny(cv_image,100,200)
    pyplot.subplot(1,2,1),pyplot.imshow(cv_image,'gray')
    pyplot.title('original')
    pyplot.xticks([]),pyplot.yticks([])

    pyplot.subplot(1,2,2),pyplot.imshow(canny,'gray')
    pyplot.title('processed')
    pyplot.xticks([]),pyplot.yticks([])

    pyplot.pause(0.05)
    #time.sleep(0.9)
    #pyplot.close('all')

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("webcam", Image, process)

    rospy.spin()

if __name__ == '__main__':
    bridge = CvBridge()

    listener()