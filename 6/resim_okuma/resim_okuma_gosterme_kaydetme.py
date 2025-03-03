import cv2


img = cv2.imread("images.jpg", 0) # 0 gri tonlama için kullanılır
# print(img) resimlerde birer matristen oluşur
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
cv2.imwrite("images1.jpg", img)
cv2.waitKey(0)
# sıfır degeri girilirse ekranı kapatmadığımız sürece açık kalır
cv2.destroyAllWindows()
