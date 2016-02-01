const int WNM = 2;
const int scan = 3;
const int pen = A0;
const int T = 10; // period of reading data
int wLen = 1;
float wNum = 4000.0;
int dt=0;
void setup() {
  Serial.begin(9600);
  pinMode(wNum, INPUT);
  pinMode(scan, INPUT);
  wLen = timeStep();
  dt = 50/wLen;
}

void loop() {
  if (digitalRead(scan)==LOW && wNum > 200 ) {
    
    Serial.print(wNum);
    Serial.print('\t');
    Serial.print(float(analogRead(pen))/10.24);
    wNum -= dt;
    
    delay(T);
  }
  
  

  
}

int timeStep() {
  int t = 0;
  int t0 = 0; 
  int t1 = 0;
  int t2 = 0;
  int xOld = HIGH;
  int x = HIGH;
  bool k = 0;// defines start and end of measuring time step
  while(1) {
    x = digitalRead(WNM); 
    if (x == LOW && xOld == HIGH && k == 0) {t0 = t; k = 1;}
      else if(x == HIGH && xOld == LOW && k == 1)  {t1 = t;}
        else if(x == LOW && xOld == HIGH && k == 1)  {
          t1 = t; 
          k = 0; 
          break;
          }
      
    delay(T);
    t+=T;
    xOld = x;  
    }
  int peak = t1 - t0;
  int wLen = t2 - t0;
  return wLen;    
}



 


