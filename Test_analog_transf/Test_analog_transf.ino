#define WNm_pin 2                  // pin of wavenumver 
//(orange - sig, orange+white -GND)
#define pen_pin A0                 // pin of analog intensyvity (Blue)+



volatile float wNum = 4000.0;     // wavenumver
volatile float pen = 0.0;         // relate  Transmiteence
float pen_old = 0.0;


//////////////////////////// Setup //////////////////////////////////////////////////
void setup() {
  Serial.begin(38400);

  pinMode(WNm_pin, INPUT_PULLUP);
  attachInterrupt(0, read_data, FALLING);
  Serial.println("Setup started");
}
///////////////////////////  Main  Loop //////////////////////////////////////////
void loop() {
//  if (pen_old != pen){
    Serial.print(wNum);
    Serial.print('\t');
    Serial.println(pen);
//    pen_old = pen;
//  }
}
////////////////////////// Read data ////////////////////////////////////////////
void read_data() {
  pen = analogRead(pen_pin);
  wNum -= 0.1;
//  Serial.print("__|");

}









