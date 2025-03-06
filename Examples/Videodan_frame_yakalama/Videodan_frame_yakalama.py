import cv2
cap= cv2.VideoCapture(0)
frame_count = 0
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        breakqq
    elif cv2.waitKey(30) & 0xFF == ord("r"):
        filename = f"frame_{frame_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"kaydedildi: {filename}")
        frame_count +=1

cap.release()
cv2.destroyAllWindows()