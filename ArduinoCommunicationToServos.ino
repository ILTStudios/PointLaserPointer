#include<Servo.h>

// setup vars for motors, read string, and rot val and bool trigger
Servo MotorOne;
Servo MotorTwo;
String readString;
int Rot;
char val;
bool OneOrTwo = false;

// attach and write servos to ready pos, and begin serial bus comm. at 9600 baud
void setup() {
  Serial.begin(9600);
  MotorOne.write(100);
  MotorTwo.write(0);
  MotorOne.attach(9);
  MotorTwo.attach(10);
}

void loop(){
  
  // when serial comm detected then do -
  while(Serial.available()) {
    val = Serial.read();
    readString += val;
    delay(2);
  }
  
  // if text detected then do -
  if (readString.length()> 0) {
    Serial.println(readString);
    int n = readString.toInt();
    Serial.println(n);
    
    // bool trigger method system
    if (OneOrTwo == false){
      MotorOne.write(n);
      OneOrTwo = true;
    }
    else{
      MotorTwo.write(n);
      OneOrTwo = false;
    }
  }
  readString = "";
}
