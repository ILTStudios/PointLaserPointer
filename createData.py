import cv2, math
from serial import Serial
import time

haarfile = (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
(width, height) =  (100, 100)

arduino = Serial('COM5', 9600)
arduino.timeout = 1

face_cascade = cv2.CascadeClassifier(haarfile)
Camera = cv2.VideoCapture(0)

count = 1
while True:
    (_, im) = Camera.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (255,0,0), 2)

        #print(x,y,w,h)

        xTwo = (x + w)
        yTwo = (y + h)
        mainCircle = (320, 240)
        faceCircle = (int((x + xTwo) / 2), int((y + yTwo)/ 2))
        distanceX = int((x + xTwo) / 2) - 320
        distanceY = 240 - int((y + yTwo) / 2)
        hypotenuseX = math.hypot(distanceX, distanceY)
        hypotenuseY = math.hypot(distanceY, distanceX)
        centerX = int((x + xTwo) / 2)
        centerY = int((y + yTwo) / 2)

        #print(faceCircle)

        cv2.circle(im, faceCircle, 2, (255,0,0), 4)
        cv2.circle(im, mainCircle, 2, (255,0,0), 4)
        cv2.line(im, mainCircle, (int((x + xTwo) / 2), 240), (0, 255, 0), 2)
        cv2.line(im, mainCircle, (320, int((y + yTwo) / 2)), (0, 0, 255), 2)
        cv2.line(im, (int((x + xTwo) / 2), 240), (320, int((y + yTwo) / 2)), (150, 150, 150), 2)        

        #print(distanceX, distanceY)

        #cv2.putText(im, str(distanceX), (centerX, 240), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA, False)
        #cv2.putText(im, str(distanceY), (320, centerY), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA, False)
        #cv2.putText(im, str(math.hypot(distanceX, distanceY)), (centerX, centerY), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA, False)

        #print((math.sin(distanceX/hypotenuseX)), (math.sin(distanceY/hypotenuseY)))

        #face = gray[y:y + h, x:x + w]
        #face_resize = cv2.resize(face, (width, height))

        xSinRatio = distanceX / w
        ySinRatio = distanceY / w
        xyArray = [100 + int(100 * math.sin(ySinRatio)), int(100 * math.sin(xSinRatio))]
        print(xyArray)
        for x in xyArray:
            arduino.write(str(x).encode())
            time.sleep(0.2)
    count += 1

    cv2.imshow('OpenCV', im)
    cv2.waitKey(1)