#include <Servo.h>

//servos
#define SERVO_TILT 2
#define SERVO_PAN 3
#define SERVO_FIRE 4

int servoPosTilt;
int servoPosPan;
int servoPosFire;

Servo servoTilt;
Servo servoPan;
Servo servoFire;

//ultrasonic sensor
#define TRIG_PIN 5
#define ECHO_PIN 6

float duration, distance;

//Object Location Initializations
String objectPos;
int objectPosX = 0;
int objectPosY = 0;

#define OBJ_TOLERANCE 30

void setup() {
  //Serial initializations
  Serial.begin(9600);

  //Servo Initializations
  servoTilt.attach(SERVO_TILT);
  servoPan.attach(SERVO_PAN);
  servoFire.attach(SERVO_FIRE);

  servoPosTilt = 90;
  servoPosPan = 135;
  servoPosFire = 0;

  //Ultrasonic Initialization
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  //Communication between Python Code and arduino
  if (Serial.available() > 0) {
    objectPos = Serial.readString();
    objectPosX = objectPos.substring(0, 4).toInt();
    objectPosY = objectPos.substring(5, 9).toInt();

    if (objectPosX > 0) {
      servoPosPan += 10;
    } else {
      servoPosPan;
    }

    if (objectPosY > 0) {
      servoPosTilt++;
    }else{
      servoPosTilt--;
    }
  }

  servoTilt.write(servoPosTilt);
  servoPan.write(servoPosPan);

  //firing mechanism
  int objectDistance = distanceDetection();
  if (objectDistance < 5){
    firingMechanismActivate();
  } else {
    firingMechanismStop();
  }
}

int distanceDetection(){
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  distance = (duration*.0343)/2;

  return distance;
}

void firingMechanismActivate(){
  for (servoPosFire = 0; servoPosFire <= 180; servoPosFire += 5) {
    servoFire.write(servoPosFire);
    delay(15);
  }
  for (servoPosFire = 180; servoPosFire >= 0; servoPosFire -= 5) {
    servoFire.write(servoPosFire);
    delay(15);
  }
}

void firingMechanismStop(){
  servoFire.write(0);
}