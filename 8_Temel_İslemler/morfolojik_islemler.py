import cv2
import numpy as np

img = cv2.imread("C:\\Egitim\\OpenCV\\Exams\\Videodan_frame_yakalama\\frame_0.jpg",0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1) # bozulmaya sebep olur siyahlıklar artar
dilation = cv2.dilate(img,kernel, iterations=1)# kalınlaştırır beyazlar artar
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)# resim üzerindeki gürültüleri kaldırır
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)#resim üzerindeki bozulmalargiderilir
# morphology de GRADIENT fonksiyonu en dışını siyah yapar, TOPHAT ise resim üzerinde bazı noktalar silinir
cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilate", dilation)
cv2.imshow("morphology", closing)
cv2.waitKey(0)