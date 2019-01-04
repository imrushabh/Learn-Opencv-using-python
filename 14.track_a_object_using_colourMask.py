import cv2
import numpy as np

def main():
    windowName="original web cam feed"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)#we can use multiple web cams
    
    
    
    if cap.isOpened():
        ret,frame=cap.read()
    while ret:
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #blue color
        low=np.array([100,50,50])
        high=np.array([140,255,255])
        
        image_mask=cv2.inRange(hsv,low,high)
        output=cv2.bitwise_and(frame,frame,mask=image_mask)
        cv2.imshow("blue mask",image_mask)
        cv2.imshow("real object",output)
        cv2.imshow(windowName,hsv)
        if cv2.waitKey(1)==27:
            break;
    cap.release()
    
    cv2.destroyWindow(windowName)
    
if __name__=="__main__":
    main()
