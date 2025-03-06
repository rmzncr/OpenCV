import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = np.zeros((500,500),np.uint8)
img = cv2.imread("C:\\Egitim\\OpenCV\\Exams\\Videodan_frame_yakalama\\frame_0.jpg")# sonuna 0 paramaetresi atanırsa bu onun siyah-beyaz yapar
#cv2.rectangle(img,(0,60),(200,150),(255,255,255), -1)
b,g,r=cv2.split(img)

cv2.imshow("img", img)
plt.hist(b.ravel(),256,[0,256]) # matrisi tek bir satıra döker
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()