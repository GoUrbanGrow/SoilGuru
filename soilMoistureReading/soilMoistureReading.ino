

/* Project: SoilGuru 
Author: Kartik & Michiel
Description: this is an arduino sketch that reads from an analog.
Pin and writes it to a serial buffer. The data retrieved comes from a simple soil moisture sensor.
The soil moisture sensor measures resistence between two ports.
For more information see: .....
*/

// Analog pin number A0 that the moisturesensor is attached to.
int moistureSensorPin = 0;

// Analog reading from sensor between 0 and 1023. 
// 0 indicates 0% moisture, and 1023 indicates 100% moisture.
int moisture_val;

// Serial buffer is opened with a specified bit rate.
void setup() {
  Serial.begin(9600);  
}

// Read from the analoge sensor and write the data to the serial buffer.
// Delay of 5 seconds implemented to insure that buffer is flushed between succesive readings.
void loop() {
  moisture_val = analogRead(moistureSensorPin);
  Serial.println(moisture_val);
  delay(5000);
}
