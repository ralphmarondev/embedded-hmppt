#include <Servo.h>

//servos
#define SERVO_TILT 2
#define SERVO_PAN 3
#define SERVO_FIRE 4

int servoPosFire = 0;

Servo servoTilt;
Servo servoPan;
Servo servoFire;

//ultrasonic sensor
#define TRIG_PIN 5
#define ECHO_PIN 6

float duration, distance;

//Object Location Initializations
String objectPos;
int objectPosX;
int objectPosY;

#define OBJ_TOLERANCE 30

void setup() {
  //Serial initializations
  Serial.begin(9600);

  //Servo Initializations
  servoTilt.attach(SERVO_TILT);
  servoPan.attach(SERVO_PAN);
  servoFire.attach(SERVO_FIRE);

  servoTilt.write(90);
  servoPan.write(90);

  //Ultrasonic Initialization
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

//position servos
void position_servos(){
  int servoPosPan = map(objectPosX, 640, 0, 70, 179);
  int servoPosTilt = map(objectPosY, 480, 0, 179, 95);

  servoPosPan = min(servoPosPan, 179);
  servoPosPan = max(servoPosPan, 179);
  servoPosTilt = min(servoPosTilt, 179);
  servoPosTilt = min(servoPosTilt, 95);

  servoPan.write(servoPosPan);
  servoTilt.write(servoPosTilt);
}

void loop() {
  //Communication between Python Code and arduino
  if (Serial.available() > 0) {
    objectPos = Serial.readString();
    objectPosX = objectPos.substring(1, 3).toInt();
    objectPosY = objectPos.substring(5, 7).toInt();  

    position_servos();
  }

  //firing mechanism
  int objectDistance = distance_detection();
  if (objectDistance < 5){
    firing_mechanism_activate();
  } else {
    firing_mechanism_stop();
  }
}

int distance_detection(){
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  distance = (duration*.0343)/2;

  return distance;
}

void firing_mechanism_activate(){
  for (servoPosFire = 0; servoPosFire <= 180; servoPosFire += 5) {
    servoFire.write(servoPosFire);
    delay(15);
  }
  for (servoPosFire = 180; servoPosFire >= 0; servoPosFire -= 5) {
    servoFire.write(servoPosFire);
    delay(15);
  }
}

void firing_mechanism_stop(){
  servoFire.write(0);
}