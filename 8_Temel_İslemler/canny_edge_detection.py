import cv2
cap = cv2.VideoCapture(0)
#edges kenarları bulan bir fonksiyondur
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # görüntüye takla attırır sağ elimiz sağdan kalkar
    edges = cv2.Canny(frame,100,200)

    cv2.imshow("Frame", frame)
    cv2.imshow("Edges",edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()