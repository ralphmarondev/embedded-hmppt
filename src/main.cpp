#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the built-in LED pin as an output
  Serial.begin(9600);  // Initialize serial communication at 9600 bits per second
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    if (receivedChar == '1') {
      digitalWrite(LED_BUILTIN, HIGH);  // Turn on the LED
      delay(500);  // Wait for half a second
      digitalWrite(LED_BUILTIN, LOW);   // Turn off the LED
      delay(500);  // Wait for half a second
    } else if (receivedChar == '0') {
      digitalWrite(LED_BUILTIN, LOW);   // Turn off the LED
    }
  }
}
