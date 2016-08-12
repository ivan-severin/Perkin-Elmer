#define WNm_pin 2        // pin of wavenumver
#define scan_pin 3       // pin of pauses in mesuring
#define pen_pin A0       // pin of analog intensyvity

#define T  25            // period of reading data
float dt = 0.0;

int wLen = 1;            // lengh of periodic peaks

float wNum = 4000.0;     // wavenumver
float pen = 0.0;

bool x = HIGH;
bool xOld = HIGH;


////////////////////////////  Settings //////////////////////////////////////////////


unsigned short scanTtime = 6;
unsigned short multipler = 1;
unsigned short chExp = 1;

int i = 0.0;

bool timeDrive = 0;
bool index = 0;
bool abs_ = 0;

//////////////////////////// Setup //////////////////////////////////////////////////
void setup() {
  Serial.begin(38400);
  pinMode(WNm_pin, INPUT);
  pinMode(scan_pin, INPUT);
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
  //delay(T);

}
////////////////////////// Read data ////////////////////////////////////////////
void read_data() {
  if (digitalRead(scan_pin) == LOW ) {


    x = digitalRead(WNm_pin);

    for (int i=0;i<5;i++){
      if (x == LOW && xOld == HIGH){
        x = digitalRead(WNm_pin);
        pen = analogRead(pen_pin);
        

      }
    }

    wNum -= 0.5;
    Serial.print(wNum);
    Serial.print('\t');
    Serial.println(pen);

  }


  xOld = x;
}


////////////////////////// Send data ////////////////////////////////////////////
void send_data() {

}




////////////////////////// Get Status ////////////////////////////////////////////
bool getStatus() {


}

////////////////////////// Get Settings //////////////////////////////////////////
bool getSettings() {
  int incomingByte = 0;
  if (Serial.available() > 0) {

    delay(10);

    //for ( int i = 0; i < Serial.available(); i++ )  {   /// check this num

    if (Serial.read() == 0xAC) {

      incomingByte = Serial.read();

      //      switch (incomingByte) {
      //        case 0x01:
      //          measure = true;
      //          channel = 0;
      //          break;
      //
      //        case 0x02:
      //          measure = true;
      //          channel = 0;
      //          break;
      //      }
    }
  }

  return 0;
}


/////////////// Get time of Wave number step motor [Use it for debug] ////////////////////////
float timeStep() {

  unsigned long int t0 = 0; //time of starting measure [High -> Low]
  unsigned long int t1 = 0; //time of begin impulse [Low -> High]
  unsigned long int t2 = 0; // time of width peak during [High]

  bool xOld = HIGH;
  bool x = HIGH;            // get signal (periodic low)
  bool k = 0;  // defines start and end of measuring time step

  while (true) {
    x = digitalRead(WNm_pin);

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















