int moistureSensorPin = 0;
int moisture_val;

void setup() {
  Serial.begin(9600);  
}

void loop() {
  moisture_val = analogRead(moistureSensorPin);
  Serial.println(moisture_val);
  delay(5000);
}
