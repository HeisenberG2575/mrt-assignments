#!/usr/bin/env python
import cv2
import matplotlib.pyplot as plot
import time
def main():
    image=cv2.imread('/home/heisenberg/catkin_ws/src/urdf_tutorial/singlemarkersoriginal.jpg')
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    aruco_params = cv2.aruco.DetectorParameters_create()
    corners, ids, rejected = cv2.aruco.detectMarkers(image, aruco_dict,parameters=aruco_params)
    if len(corners)>0:
        ids=ids.flatten()
        print(ids)
        cv2.aruco.drawDetectedMarkers(image,corners)
        cv2.imshow('aruco',image)
        time.sleep(5)
if __name__=='__main__':
    import cv2
    
    main()
