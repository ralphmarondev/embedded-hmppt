void setup(){
  Serial.begin(9600);
}

void loop(){
  if(Serial.available() > 0){
    char recieved = Serial.read();

    Serial.print("Recieved: ");
    Serial.println(recieved);
  }
}