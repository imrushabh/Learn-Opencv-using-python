import cv2
def main():
    windowName="live vido feed"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)#we can use multiple web cams
    #check if cam is open
    if cap.isOpened():
        ret,frame=cap.read()
    while ret:
        ret,frame=cap.read()
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",img)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break;
    cap.release()
    
    cv2.destroyWindow(windowName)
    
if __name__=="__main__":
    main()
