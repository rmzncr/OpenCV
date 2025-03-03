import cv2

"#WEB CAM"
cap = cv2.VideoCapture(0) #webcam kullanılacaksa 0 değeri girilir

while True:
    ret, frame =cap.read()
    frame=cv2.flip(frame,2) # görüntüyü istediğin eksende yansıtır
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): # "q" tuşuna basıldığında ekranı kapat
        break
cap.release()
cv2.destroyAllWindows()
"""
# video oynatma
cap= cv2.VideoCapture("antalya.mp4")

while True:
    ret, frame= cap.read()
    if ret== 0:
        break
    frame=cv2.flip(frame,1)
    cv2.waitKey(20)
    cv2.imshow("ANTALYA",frame)
cap.release()
cv2.destroyAllWindows()

"""
