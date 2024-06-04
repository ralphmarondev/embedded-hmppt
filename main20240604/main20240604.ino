#define PIN 13

void setup(){
  Serial.begin(9600);
  pinMode(PIN, OUTPUT);
}

void loop(){
  if(Serial.available() > 0){
    String msg = Serial.readString();

    if (msg == "ON"){
      digitalWrite(PIN, HIGH);
    }
    else if (msg == "OFF"){
      digitalWrite(PIN, LOW);
    }
    else{
      digitalWrite(PIN, HIGH);
      delay(1000);
      digitalWrite(PIN, LOW);
    }
  }
}