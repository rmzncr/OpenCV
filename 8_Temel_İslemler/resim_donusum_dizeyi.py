import cv2
import numpy as np

img = cv2.imread("C:\\Egitim\\OpenCV\\Exams\\Videodan_frame_yakalama\\frame_0.jpg",0)
row,col = img.shape 

M= np.float32([[1,0,50],[0,1,200]]) # buradaki 50 ve yüz değeri resmin dışarda kalan alanının ne kadar olacağını gösterir

dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()