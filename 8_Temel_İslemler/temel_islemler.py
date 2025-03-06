import cv2

img= cv2.imread("images.jpg")


dimension= img.shape # resmin kaça kaçlık oduğunu gösterir
print(dimension)
color = img[150, 200] # piksel değerlerinin hangi renkte olduğu
print("BGR:", color)

blue = img[150, 200, 0]
print("blue:", blue)

green = img[150, 200, 1]
print("green:", green)
red = img[150, 200, 2]
print("red:", red)

img[150, 200, 0] = 250
print("new blue:",img[150, 200, 0])

blue1= img.item(100,180,0)
print("blue1:",blue1)

img.itemset((100,180,0),172)
print("new blue1:", img[100,180,0])
cv2.imshow("klon asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()