// Polled LED.  Make LED turn on and off based on keyboard input.  
// On-off achieved by giving 5V to the circuit with a digital ouput.
// One solution is to change the LED circuit state every time you see a keystroke.
// Another solution is to read the keyboard input and have the LED change state based
// on specific keyboard input.

// Initialize variables to store the pin number and the keyboard input.




void setup() {

	// Initiate communication with the serial monitor.
  	Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  
  	// Set the state of your digital pin to output.

}

void loop() {

        // Monitor the serial connection.  If it is open, read from serial port
        // If the On-off Pin is high, set it to low.  Otherwise, set it to high.
        // This will guarantee that the pin always changes state.
        
        if (Serial.available() > 0) {
                // read the incoming byte:
               
               }
                          
        
}
