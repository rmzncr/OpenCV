import cv2
cv2.namedWindow("images")
img=cv2.imread("images.jpg")
img=cv2.resize(img,(600,400)) # resimi boyutlandırmak için kullanılır
cv2.imshow("images",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
