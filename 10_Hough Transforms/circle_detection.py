import cv2
import numpy as np

img1 = cv2.imread("C:\\Egitim\\OpenCV\\10_Hough Transforms\\5.1 coins.jpg.jpg")
img2 = cv2.imread("C:\\Egitim\\OpenCV\\10_Hough Transforms\\5.2 balls.jpg.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1, 5)
img2_blur = cv2.medianBlur(gray2, 5)
#param1 = gradient değerini, param2= ise threshold değerini gösterir kritik değerlerdir
circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT,1,img1.shape[0]/4, param1 = 200, param2= 10,minRadius=15,maxRadius=80) # 5 ile 30 arası yarıçap

if circles is not None: # değerler boş değilse
    circles = np.uint16(np.around(circles))# circles içinde tutulan değerleri yuvarlar
    for i in circles[0,:]: # 0 değerden nereye kadar değer varsa tek tek i ye atanır
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow("img1",img1)
cv2.waitKey(0)