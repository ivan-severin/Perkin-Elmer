const int WNM = 2;  // pin of wavenumver
const int scan = 3; // pin of pauses in mesuring
const int pen = A0; // pin of analog intensyvity
const int T = 50; // period of reading data
int wLen = 1;       // lengh of periodic peaks
float wNum = 3800.0;
float dt = 0.0;

////////////////////////////  Settings //////////////////////////////////////////////
int measure;
int channel;
unsigned short scanTtime = 6;
unsigned short multipler = 1;
unsigned short chExp = 1;
bool timeDrive = 0;
bool index = 0;
bool abs_ = 0;




//////////////////////////// Setup //////////////////////////////////////////////////
void setup() {
  Serial.begin(9600);
  pinMode(wNum, INPUT);
  pinMode(scan, INPUT);
  Serial.println("Setup started");
  //wLen = timeStep();
  //wLen = 1199;
  //dt = 100.0 / float(wLen);
}
///////////////////////////  Main  Loop //////////////////////////////////////////
void loop() {

  //if (Serial.available() > 0  ){
  //bool cmd = Serial.read();
  //}

  read_data();
  //send_data();
  //dt += 1.0;
  delay(T);

}
//////////////////////////////////////////////////////////////////////
void read_data() {
  if (digitalRead(scan) == LOW  ) {

    Serial.print(dt);
    Serial.print('\t');
    Serial.println(analogRead(pen));
    dt += 1.0;
    }
  else {
    //Serial.println("scan OFF");
  }
}

bool getStatus() {


}


bool getSettings() {
  int incomingByte = 0;
  if (Serial.available() > 0) {

    delay(10);

    //for ( int i = 0; i < Serial.available(); i++ )  {   /// check this num

    if (Serial.read() == 0xAC) {

      incomingByte = Serial.read();

      switch (incomingByte) {
        case 0x01:
          measure = true;
          channel = 0;
          break;

        case 0x02:
          measure = true;
          channel = 0;
          break;
      }
    }
  }

  return 0;
}

void send_data() {

  Serial.print(dt);
  Serial.print('\t');
  Serial.println(float(analogRead(pen)) / 10.23);


}


float timeStep() {

  unsigned long int t0 = 0;
  unsigned long int t1 = 0;
  unsigned long int t2 = 0;
  bool xOld = HIGH;
  bool x = HIGH;            // get signal (periodic low)
  bool k = 0;               // defines start and end of measuring time step
  while (1) {
    x = digitalRead(WNM);
    if (x == LOW)                //
      Serial.println("low");
    else
      Serial.println("high");
    if (x == LOW && xOld == HIGH && k == 0) {
      t0 = millis();
      Serial.print("t0 =  ");
      Serial.println(t0);
      k = 1;
    }
    else if (x == HIGH && xOld == LOW && k == 1)  {
      t1 = millis();
      Serial.print("t1 =  ");
      Serial.println(t1);
    }
    else if (x == LOW && xOld == HIGH && k == 1)  {
      t2 = millis();
      k = 0;
      Serial.print("t2 =  ");
      Serial.println(t2);
      break;
    }

    delay(T);

    xOld = x;
  }
  Serial.println("breaked");
  int peak = t1 - t0;
  int wLen = t2 - t0;
  //wLen = 500;
  Serial.println(float(wLen) / float(T));
  return float(wLen) / float(T);
}











