#ifndef TEST2
#define TEST2
#include <Arduino.h>
#include <Servo.h>

Servo myServo;

void setup_test2(){
  Serial.begin(9600);
  myServo.attach(9); // attach servo to pin 9
}

void loop_test2(){
  if(Serial.available() > 0){
    int angle = Serial.parseInt(); // read the angle from serial
    Serial.println(angle);
    if (angle >= 0 && angle <= 180){
      Serial.println("Inside if condition");
      myServo.write(angle); // set the servo to the recieved angle
    }
  }
}
#endif