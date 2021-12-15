#include<Servo.h>

Servo MotorOne;
Servo MotorTwo;
String readString;
int Rot;
char val;
bool OneOrTwo = false;

void setup() {
  Serial.begin(9600);
  MotorOne.write(100);
  MotorTwo.write(0);
  MotorOne.attach(9);
  MotorTwo.attach(10);
}

void loop() {
  while(Serial.available()) {
    val = Serial.read();
    readString += val;
    delay(2);
  }
  if (readString.length()> 0) {
    Serial.println(readString);
    int n = readString.toInt();
    Serial.println(n);
    if (OneOrTwo == false){
      MotorOne.write(n);
      OneOrTwo = true;
    }
    else{
      MotorTwo.write(n);
      OneOrTwo = false;
    }
    /*if (n >= 500){
      Serial.println(n);
      MotorOne.writeMicroseconds(n);
      MotorTwo.writeMicroseconds(n);
    }
    else {
      Serial.println(n);
      MotorOne.write(n);
      MotorTwo.write(n);
    }*/
  }
  readString = "";
}
