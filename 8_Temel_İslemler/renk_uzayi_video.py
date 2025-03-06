import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # frameleri arka arkaya gri gösterir bu şekilde renk uzayı değişir
    if ret == False: # video bitince hata vermemesi için
        break

    cv2.imshow("Video", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()