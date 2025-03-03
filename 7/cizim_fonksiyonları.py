import cv2
import numpy as np

canvas=np.zeros((512,512,3), dtype=np.uint8) +255
#print(canvas) # beyaz olmasını istersek 255 değerini ekleri her matris için
 # siyah bir tuval gösterir

cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)# başlangıç , bitiş,renk,kalınlık
cv2.line(canvas,(100,50),(200,250),(0,0,255),thickness=7)


cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),thickness=2) # şeklin içinin dolu olması için thickness=-1 olmalıdır
cv2.circle(canvas,(250,250),(100),(0,0,255), thickness=3)

#üçgen için ayrıyetten bir fonksiyon yokturr!!!
p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)
#rastgele şekil için polylines kullanılır fakat numpy kütüphanesi içinde bulunan array içinde kullanlılr
points=np.array([[[110,200], [330,200],[290,220],[220,250]]],np.int32)
cv2.polylines(canvas,[points],True,(0,0,100),5)


cv2.ellipse(canvas,(175,150),(80,25),10,90,360,(255,255,0),-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

