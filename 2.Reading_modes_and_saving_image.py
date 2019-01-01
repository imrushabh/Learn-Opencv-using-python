import cv2
def main():
    imgpath="C:\\Users\\rusha\\Desktop\\7th sem\\virat.jpg"
    img=cv2.imread(imgpath,0) # 0 for gray image, 1 for colour image
    cv2.imshow('llena',img)
    savepath="C:\\Users\\rusha\\Desktop\\virat.jpeg" # any format of image can be specified
    cv2.imwrite(savepath,img);
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()    
