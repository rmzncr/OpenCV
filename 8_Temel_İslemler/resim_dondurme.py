
import cv2
import numpy as np

img = cv2.imread("C:\\Egitim\\OpenCV\\Exams\\Videodan_frame_yakalama\\frame_0.jpg",0)
row,col = img.shape

M= cv2.getRotationMatrix2D((col/5,row/3),180,1) # 2. değer kaç derece döneceğini 3. değer ise ne kadar büyütüleceğini
                                                                    # döndürme işlemi saat yönünün tersi yünündedir
dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)
