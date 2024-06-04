#include <Servo.h>

Servo servoMotor;
int i = 0;

void setup() {
  Serial.begin(9600);
  servoMotor.attach(9);  // Attach servo to pin 9
}

void loop() {
    int angle = i;
    if (angle >= 0 && angle <= 180) {
      servoMotor.write(angle);
    }
    Serial.println(angle);
    i++;
}

/*
recieve:
diffy
- camera center y and object center y

*/