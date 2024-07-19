import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor= 1.3, 
        minNeighbors= 5,
        minSize= (30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors= 15,
            minSize= (25, 25)
            )
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors= 15,
            minSize= (25, 25)
            )
        for(sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    cv2.imshow('video', frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()