#define LED_OUT_X 2
#define LED_OUT_Y 3

String loc;
int locX, locY;

void setup(){
  Serial.begin(9600);
  pinMode(LED_OUT_X, OUTPUT);
  pinMode(LED_OUT_Y, OUTPUT);
}

void loop(){
  if (Serial.available() > 0) {
    loc = Serial.readString();
    locX = loc.substring(0, 4).toInt();
    locY = loc.substring(5, 9).toInt();

    if(locX > 0){
      digitalWrite(LED_OUT_X, HIGH);
    }else{
      digitalWrite(LED_OUT_X, LOW);
    }

    if(locY > 0){
      digitalWrite(LED_OUT_Y, HIGH);
    }else{
      digitalWrite(LED_OUT_Y, LOW);
    }
  }
}