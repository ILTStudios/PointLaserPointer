import cv2, math, time
from serial import Serial

#Get Haar File from haar cascades
haarfile = (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#set width and height
(width, height) =  (100, 100)

#create serial bus communication with arduino on com5 using 9600 baud
arduino = Serial('COM5', 9600)
arduino.timeout = 1

#set up face cascade
face_cascade = cv2.CascadeClassifier(haarfile)

#get video capture feed
Camera = cv2.VideoCapture(0)

count = 1
while True:
    
    #read camera feed and turn into im var
    (_, im) = Camera.read()
    
    #convert to grey scale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    #use detectMultiScale() to get bounds of faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    
    #iterate through detectMultiScale() array
    for (x,y,w,h) in faces:
        
        #create rectangle of face using bounds of face
        cv2.rectangle(im, (x, y), (x+w, y+h), (255,0,0), 2)
        
        #setup repeated variables for convenience
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

        #place circle on mean pos of face
        cv2.circle(im, faceCircle, 2, (255,0,0), 4)
        
        #place circle on mean pos of cam pov
        cv2.circle(im, mainCircle, 2, (255,0,0), 4)
        
        #x axis distance line
        cv2.line(im, mainCircle, (int((x + xTwo) / 2), 240), (0, 255, 0), 2)
        
        #y axis distance line
        cv2.line(im, mainCircle, (320, int((y + yTwo) / 2)), (0, 0, 255), 2)
        
        #hypotenuse of traingle line
        cv2.line(im, (int((x + xTwo) / 2), 240), (320, int((y + yTwo) / 2)), (150, 150, 150), 2)        

        
        """ text representation of pixel values of distances, for x, y and then hypotenuse respectively (slows down face detection quite a bit)
        cv2.putText(im, str(distanceX), (centerX, 240), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA, False)
        v2.putText(im, str(distanceY), (320, centerY), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA, False)
        cv2.putText(im, str(math.hypot(distanceX, distanceY)), (centerX, centerY), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA, False)
        """
        
        #get both x and y sin ratios
        xSinRatio = distanceX / w
        ySinRatio = distanceY / w
        
        #set into array for convenience of arduino reading
        xyArray = [100 + int(100 * math.sin(ySinRatio)), int(100 * math.sin(xSinRatio))]
        #rint(xyArray)
        
        #iterate and feed data to arduino
        for x in xyArray:
            arduino.write(str(x).encode())
            time.sleep(0.2)
    count += 1

    #show image
    cv2.imshow('OpenCV', im)
    cv2.waitKey(1)
