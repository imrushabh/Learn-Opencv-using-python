import cv2
def main():
    windowName="live vido feed capture"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)#we can use multiple web cams
    
    filename="C:\\Users\\rusha\\Desktop\\virat1.avi"
    
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution=(640,480)
    VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)
    
    if cap.isOpened():
        ret,frame=cap.read()
    while ret:
        ret,frame=cap.read()
        VideoFileOutput.write(frame)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break;
    cap.release()
    
    cv2.destroyWindow(windowName)
    
if __name__=="__main__":
    main()
    
