#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge
from matplotlib import pyplot
import time
import sys
aruco_type=cv2.aruco.DICT_5X5_250
def process(data):
    aruco_params=cv2.aruco.DetectorParameters_create()
    #cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
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


    #pyplot.imshow(cv_image,'gray')
    #pyplot.title('original')
    #pyplot.xticks([]),pyplot.yticks([])    
    arucoDict=cv2.aruco.Dictionary_get(aruco_type)
    corners,ids,rejected=cv2.aruco.detectMarkers(cv_image,arucoDict,parameters=aruco_params)
    print('c',corners,'id',ids,'rej',rejected)
    if np.all(ids is not None):
        for i in range(0,len(ids)):
            rvec,tvec,marker_pts=cv2.aruco.estimatePoseSingleMarkers(corners[i],0.02)
            (rvec-tvec).any()
        print(ids)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("mybot/camera/image_raw", Image, process)

    rospy.spin()

if __name__ == '__main__':
    bridge = CvBridge()

    listener()