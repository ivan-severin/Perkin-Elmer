const int WNM = 2;
const int scan = 3;
const int pen = A0;
const int T = 10; // period of reading data
int wLen = 1;
float wNum = 4000.0;
float dt = 0.0;
void setup() {
  Serial.begin(9600);
  pinMode(wNum, INPUT);
  pinMode(scan, INPUT);
  Serial.println("Setup started");
  //wLen = timeStep();
  wLen = 1199;
  dt = 100.0 / float(wLen);
}

void loop() {
  if (digitalRead(scan) == LOW && wNum > 200 ) {

    Serial.print(wNum);
    Serial.print('\t');
    Serial.println(float(analogRead(pen)) / 10.24);
    wNum -= dt;

    
  }
  else {Serial.println("scan OFF");}


    delay(T);

}

int timeStep() {
  int t = 0;
  int t0 = 0;
  int t1 = 0;
  int t2 = 0;
  int xOld = HIGH;
  int x = HIGH;
  bool k = 0;// defines start and end of measuring time step
  while (1) {
    x = digitalRead(WNM);
    if(x==LOW) Serial.println("low");else Serial.println("high");
    if (x == LOW && xOld == HIGH && k == 0) {
      t0 = t;Serial.println("t0 seted");
      k = 1;
    }
    else if (x == HIGH && xOld == LOW && k == 1)  {
      t1 = t;Serial.println("t1 seted");
    }
    else if (x == LOW && xOld == HIGH && k == 1)  {
      t2 = t;
      k = 0;
      Serial.println("t2 seted");
      break;
    }
    
    delay(T);
    t += 1;
    xOld = x;
  }
  Serial.println("breaked");
  int peak = t1 - t0;
  int wLen = t2 - t0;
  //wLen = 500;
  Serial.println(wLen);
  return wLen;
}






