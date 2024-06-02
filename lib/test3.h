#ifndef TEST3
#define TEST3
#include <Arduino.h>
#include <Servo.h>

Servo myServo;

void setup_test3(){
    Serial.begin(9600);
    myServo.attach(9);
}

void loop_test3(){
    if(Serial.available() > 0){
        String angleString = Serial.readStringUntil('\n');
        int angle = angleString.toInt();

        if(angle >= 0 && angle <= 180){
            myServo.write(angle);
        }
    }
}
#endif