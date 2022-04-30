#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

src=cv2.VideoCapture(0)
print(src.isOpened())
bridge=CvBridge()

def talker():
    publisher=rospy.Publisher('/webcam',Image,queue_size=1)
    rospy.init_node('image',anonymous=False)
    rate=rospy.Rate(20)
    while not rospy.is_shutdown():
        flag,frame=src.read()
        if not flag:
            break
        msg=bridge.cv2_to_imgmsg(frame,'bgr8')
        publisher.publish(msg)
        rate.sleep()
    src.release()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
