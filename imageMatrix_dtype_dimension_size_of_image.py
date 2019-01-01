import cv2
def main():
    imgpath="C:\\Users\\rusha\\Desktop\\7th sem\\virat.jpg"
    img=cv2.imread(imgpath)
    cv2.imshow('llena',img)
    print(img)
    print(type(img))
    print(img.dtype)
    print(img.shape)
    print(img.ndim)
    print(img.size)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()    
