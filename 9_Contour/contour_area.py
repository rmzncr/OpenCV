import cv2

img = cv2.imread("C:\\Egitim\\OpenCV\\9_Contour\\5.1 contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,130,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
area = cv2.contourArea(cnt)# burada contoursları kjllanarak alan bulundu
print(area)
M = cv2.moments(cnt) # moments  ile alan bulucaz
print(M["m00"])
# Çevre bulma işlemi
perimeter = cv2.arcLength(cnt,True) # 2. ifade şeklin kapalıysa devam et
print(perimeter)
"""cv2.imshow("img",img)
cv2.imshow("gra", gray)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()"""