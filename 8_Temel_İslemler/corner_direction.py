import cv2
import numpy as np

img = cv2.imread("C:\\Egitim\\OpenCV\\8_Temel_İslemler\\15.1 text.png.png")
img1 = cv2.imread("C:\\Egitim\\OpenCV\\8_Temel_İslemler\\15.2 contour.png")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)# köşe tespit uygulamarı gri renkde çalışır

gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)

corners = np.int0(corners)
#köşeleri çizme işlemini yapar
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img1, (x, y), 3, (0, 0, 255), -1)

cv2.imshow("corner", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()




