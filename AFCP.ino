int incomingByte = 0; // for incoming serial data

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
}

int i = 0;
char *myStrings[] = {"chk on","alt on","hdg on","a/s on","nav on","tac on","hov on","g/s on","app on","hht on","chk off","alt off","hdg off","a/s off","nav off","tac off","hov off","g/s off","app off","hht off"};
   
// put your main code here, to run repeatedly:
void loop() {
  for (int i = 0; i < 20; i++) {   
      Serial.println(myStrings[i]);
      delay(500);
  }
  i==0;
}
