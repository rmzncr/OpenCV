#roi--> region of interest --> ilgi alanı
import cv2
img = cv2.imread("images.jpg")
roi = img[3:50, 135:190,2]# dikey: yatay

cv2.imshow("klon", img)
cv2.imshow("Roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

dimension = img.shape[:2]
print(dimension)