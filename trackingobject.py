import cv2
import numpy as np
print(cv2.__version__)
width=640
height=480
def track1(val):
    global lowhue
    lowhue=val
    print("lowhue-",lowhue)
def track2(val):
    global highhue
    highhue=val
    print("highhue",highhue)
def track3(val):
    global lowsat
    lowsat=val
    print("lowsat-",lowsat)
def track4(val):
    global highsat
    highsat=val
    print('highsat-',highsat)
def track5(val):
    global lowval
    lowval=val
    print("lowval-",lowval)
def track6(val):
    global highval
    highval=val
    print("highval-",highval)
lowhue=0
highhue=0
lowsat=0
highsat=0
lowval=0
highval=0
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("color",cv2.WINDOW_NORMAL)
cv2.createTrackbar('lowhue',"color",0,179,track1)
cv2.createTrackbar('highhue',"color",0,179,track2)
cv2.createTrackbar('lowsat',"color",0,255,track3)
cv2.createTrackbar('highsat',"color",0,255,track4)
cv2.createTrackbar('lowval',"color",0,255,track5)
cv2.createTrackbar('highval',"color",0,255,track6)
while True:
    ignore,  frame = cam.read()
    framehsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerbound=np.array([lowhue,lowsat,lowval])
    higherbound=np.array([highhue,highsat,highval])
    mymask=cv2.inRange(framehsv,lowerbound,higherbound)
    mymask=cv2.bitwise_not(mymask)
    ob=cv2.bitwise_and(frame,frame,mask=mymask)#
    cv2.imshow("my object",ob)
    cv2.imshow("my mask",mymask)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()