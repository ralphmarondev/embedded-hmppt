#define LED_OUT 13

int num = 0;

void setup(){
  Serial.begin(9600);
  pinMode(LED_OUT, OUTPUT);
}

void loop(){
  if (Serial.available() > 0) {
    num = Serial.readString().toInt();

    if (num < 4) {
      digitalWrite(LED_OUT, LOW);
    } else if (num > 4) {
      digitalWrite(LED_OUT, HIGH);
    } else {
      blink();
    }
  }
}

void blink(){
  digitalWrite(LED_OUT, HIGH);
  delay(100);
  digitalWrite(LED_OUT, LOW);
  delay(100);                   
}