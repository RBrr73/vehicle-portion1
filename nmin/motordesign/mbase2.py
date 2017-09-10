const int analogOutPin1=11;
const int analogOutPin2=9;
const int analogOutPin3=10;
const int analogInPin=A0;


int val = 0; 
int val2 = 0;
int mag = 0;
  
  
void setup(){
}
  
  void loop(){
    
val = analogRead(analogInPin); 
val2 = val-575;
mag = val2/2;

   if(mag>255){
    mag = 255;
    val = abs(val2/2)
   } 
   if(val2<0){
   analogWrite(analogOutPin2,223);
   analogWrite(analogOutPin1,mag);
   analogWrite(analogOutPin3,255);
   }
   else{
   analogWrite(analogOutPin3,116);
   analogWrite(analogOutPin1,mag);
   analogWrite(analogOutPin2,255);
   }
 Serial.println(val);
 Serial.println(mag);
    delay(8);
   rerun(2)
  }
