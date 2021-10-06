
// This is the declaration section.  Assign pin numbers to variables for use in code.

// This line assigns Analog Pin 0 to the variable aPin.
#define aPin0 0

// Do the same thing for Analog Pin 2.   We will use this to measure voltage at a different point


//  This is setup function.  It initializes the pins as well as the serial communication between
//  Arduino and the computer.
void setup() {
  
  // Tell the Serial monitor to use a baud rate of 9600.  This is the data transfer rate.
  Serial.begin(9600);
  
  // Use the pinMode function to tell Arduino to put Analog Pin 0 into INPUT mode so it can watch for
  // a signal.
  pinMode(aPin0, INPUT);
  
  // Do the same for Analog Pin 2.

  
}

// This is the loop structure that will operate continuously as long as the arduino is powered.
void loop() {
  
  //Read an integer from analogRead and record
  int Vin_digital = analogRead(aPin0);
  // Make the analog to digital conversion to report the value in Volts.
  float Vin = 5*float(Vin_digital)/1023;
  
  // Do the same for Analog Pin 2.
  
  // Print the following info to the Serial Monitor.
  Serial.print("The value of Vin is: ");
  Serial.println(Vin);

  // Do the same for Analog Pin 2.
  
  // Add a delay so it doesn't go too fast to read.
  delay(2000);  //This is a 2 second delay.  Delay works in milliseconds.

}
