import cv2
def main():
    windowName="live vido feed"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)#we can use multiple web cams
    #check if cam is open
    if cap.isOpened():
        ret,frame=cap.read()
    print("width:"+str(cap.get(3)))
    print("height:"+str(cap.get(4)))
    cap.set(3,120)
    cap.set(4,108)
    print("width:"+str(cap.get(3)))
    print("height:"+str(cap.get(4)))
    while ret:
        ret,frame=cap.read()
        
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break;
    cap.release()
    
    cv2.destroyWindow(windowName)
    
if __name__=="__main__":
    main()
    
