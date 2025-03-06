import cv2

img1 = cv2.imread("C:\\Users\\ramaz\\PycharmProjects\\OpenCV\\8_Temel_İslemler\\Bitwise\\9.1 bitwise_2.png.png")
img2 = cv2.imread("C:\\Users\\ramaz\\PycharmProjects\\OpenCV\\8_Temel_İslemler\\Bitwise\\9.2 bitwise_1.png.png")

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img2, img1)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("bit_not", bit_not2)


cv2.waitKey(0)
cv2.destroyAllWindows()
