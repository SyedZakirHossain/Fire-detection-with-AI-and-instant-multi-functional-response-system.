//for linkedin 
 int buzpin=12;
 //int threshold=200;// sets threshold value for flame sensor
int ena=5;//pwm pin
int in1=6;
int in2=7;
int light=8;
int fan=9;
//int enb=10;// pwm pin

//int flamesensvalue=0; // initialize flamesensor readin

void setup() {
  pinMode(buzpin, OUTPUT);
  Serial.begin(9600);
  //pinMode(ledpin,OUTPUT);
pinMode(in1,OUTPUT);
pinMode(in2,OUTPUT);
pinMode(ena,OUTPUT);
pinMode(fan,OUTPUT);
pinMode(light,OUTPUT);
digitalWrite(ena,0);
digitalWrite(in1,LOW);
digitalWrite(in2,LOW);
digitalWrite(fan,HIGH);
//delay(5000);
digitalWrite(buzpin, LOW);
digitalWrite(light,HIGH);


}

void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    
    if (incomingByte == '1') {
      digitalWrite(ena,250);
      digitalWrite(in1,HIGH);
      digitalWrite(in2,LOW);
      digitalWrite(fan, LOW);
      //delay(5000);
      digitalWrite(buzpin, HIGH);
      delay(500);
      digitalWrite(buzpin, LOW);
      delay(500);
      digitalWrite(light, LOW);
      delay(1000);
      digitalWrite(light, HIGH);
      delay(1000);
            
    }
    }
  }
