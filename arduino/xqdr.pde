// Arduino Quadcopter control
//   requires SimpleMessageSystem.h and Servo.h libraries
//   included by default with the Arduino package (arduino.cc)
//
//  initial testing environment:
//    - serial communication using SimpleMessageSystem.h
//  

#include <SimpleMessageSystem.h>
#include <Servo.h>

void setup()
{
  Serial.begin(9600); //115200
}

void loop()
{
  if (messageBuild() > 0) {     // Checks to see if the message is complete and erases any previous messages
    switch (messageGetChar()) { // Gets the first word as a character
    case 'r':     // read
      readpins();
      break;
    case 'w':     // write
      writepin();
    }
  }
}

void readpins(){
  switch (messageGetChar()) {     // get next word as char
    case 'd':   // digital
    messageSendChar('d');
    for (char i=2;i<14;i++) {
      messageSendInt(digitalRead(i));  // read pins 2-13
    }
    messageEnd();
    break;
  case 'a':    // analog
    messageSendChar('a');
    for (char i=0;i<6;i++) {
      messageSendInt(analogRead(i)); // read pins 0-5
    }
    messageEnd();
  }
}

void writepin() {
  int pin;
  int state;
  switch (messageGetChar()) { // get next word as char
    case 'a' : // analog
    pin = messageGetInt();   // get next word as an int
    state = messageGetInt(); // get next word as an int
    pinMode(pin, OUTPUT);    // set state
    analogWrite(pin, state); // set PWM of pin
    break;
  case 'd' :   // digital
    pin = messageGetInt();    // get next word as integer
    state = messageGetInt();  // get next word as integer
    pinMode(pin,OUTPUT);      // set state
    digitalWrite(pin,state);
  }
}

