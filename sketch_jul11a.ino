#include <Servo.h> //importing Servo Library

//declaring variables
Servo servoRight;
Servo servoLeft;

int buzzerPin = 4;

void setup() {
//put your setup code here, to run once:
 servoLeft.attach(13);
 servoRight.attach(12);

  pinMode (buzzerPin, OUTPUT);
}

void movingBack(){
     servoLeft.writeMicroseconds(1300);
     servoRight.writeMicroseconds(1700);
     delay(100);
    
     servoLeft.writeMicroseconds(1500);
     servoRight.writeMicroseconds(1500);
     delay(100);
  
    
}
void movingForward(){
     servoLeft.writeMicroseconds(1700);
     servoRight.writeMicroseconds(1300);
     delay(100);
    
     servoLeft.writeMicroseconds(1500);
     servoRight.writeMicroseconds(1500);
     delay(100); 
    
}

void turnRight() {
  servoRight.writeMicroseconds(1700);
  delay(500);
 
  
}

void turnLeft() {
  servoLeft.writeMicroseconds(1300);
  delay(500);

  
}
void backForth () {
     servoLeft.writeMicroseconds(1700);
     servoRight.writeMicroseconds(1300);
     delay(300);
    
     servoLeft.writeMicroseconds(1500);
     servoRight.writeMicroseconds(1500);
     delay(70);

     servoLeft.writeMicroseconds(1300);
     servoRight.writeMicroseconds(1700);
     delay(300);

     servoLeft.writeMicroseconds(1500);
     servoRight.writeMicroseconds(1500);
     delay(400);
}

void loop() {
  // put your main code here, to run repeatedly:

   tone (buzzerPin,5000,1000);
   delay(1000);
   noTone(buzzerPin);
   delay(1000);

movingBack();
backForth();
backForth();
turnRight();
turnRight();
movingForward();
backForth();
movingForward();
movingBack();
turnRight();
turnRight();
turnRight();
movingBack();
backForth();
turnLeft();
turnLeft();
backForth();
turnRight();

  
}
