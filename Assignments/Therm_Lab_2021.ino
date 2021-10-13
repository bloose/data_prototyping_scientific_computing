
// This is the declaration section.  Assign pin numbers to variables for use in code.

// This line assigns Analog Pin 0 to the variable aPin.




//  This is setup function.  It initializes the pins as well as the serial communication between
//  Arduino and the computer.
void setup() {
  // Tell the Serial monitor to use a baud rate of 9600.  This is the transfer rate.


  
}

// This is the loop structure that will operate continuously as long as the arduino is powered.
void loop() {
  
  
  // Use the pinMode function to tell Arduino to put Analog Pin 0 into INPUT mode so it can watch for
  // a signal.



  //Read an integer from analogRead and record


  // Make the analog to digital conversion to report the value in Volts.  See Data Measurement notes from Week04.
  
  
  // Do the same for Analog Pin 2.



  // Compute the resistance as indicated in the lab instructions and print to the Serial port.
  

  // Add a delay so it doesn't go too fast to read.



}
