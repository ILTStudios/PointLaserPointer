# PointLaserPointer
Using an Arduino Uno, a Bread Board, two servo motors and the power of being bad at coding. Even you can move a laser pointer such that it points it at your face. 

# Materials
The materials required for this project aren't that complex or hard to find. 
 > Arduino Uno
 > Bread Board
 > Servo Motors MG9S * 2
 > Connecting wires
    > One for 5V connection from A.U to B.B
    > One for Ground connection from A.U to B.B
    > Two for Pin Connection from both MG9S servos to A.U Pin connectors (9, 10)
    > Two for 5V and Ground connection to servo One, and Two for 5V and Ground Connection to Servo Two

# Connection
First connect your 5V connecting wire and Ground connecting wire to the vertical connections on the bread board.
Then connect your pin connections to each Servo motor on the desired A.U pin
Lastly connect your bread board 5V and ground connections to servo one and servo two respectively. 
Lastly, place servo one on its side and attach servo two pointing up to the blade of servo one, such that servo two can move in all y and x axis rotations. 

# Process 
Boot up Arduino IDE and paste required Arduino Code into the module. 
Setup a seriel connection with A.U using either USB type b serial bus connection or tx and rx serial bus connection.

# How It Works
The main brains of the robot is your laptop, it attains a video feed of your camera and process' it through the python wrapped version of open source computer vision library (openCV) to get a cascade classifier of the grayscale version of the image. Once that is completed it draws a rectangle with the detectMultiScale() function and detects your face. 

Then using some savy coordinate calculations it finds the mean of your FOV camera and the mean of your face, thus connecting the x and y axis with a line and measering the pixels as a measurement-unit. Then using more calculations it finds the z axis distance and pips it into a math.sin() function to find the angle of rotation for each motor. 
 > x motor - (p/h) * sin() = (x/h) * sin()
 > y motor - (p/h) * sin() = (y/h) * sin()

Then it uses the serial bus communication to feed the inputs to the motors which based on a bool trigger move each motor seperately.
Lastly, the motors move and the processing of one image is complete. 
