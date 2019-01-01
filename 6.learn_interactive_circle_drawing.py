import cv2
import numpy as np
img = np.zeros((512, 512, 3), np.uint8)
windowName = 'drawing'
cv2.namedWindow(windowName)

def draw_circle(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img,(x,y),40,(0,255,0),-1)
cv2.setMouseCallback(windowName, draw_circle)

def main():
    while(1):
        cv2.imshow(windowName,img)
        if cv2.waitKey(1) == 27:
            break
if __name__=="__main__":
    main()
