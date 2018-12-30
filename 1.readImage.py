import cv2
def main():
    imgpath="C:\\Users\\rusha\\Desktop\\7th sem\\virat.jpg"
    img=cv2.imread(imgpath)
    cv2.imshow('llena',img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()    