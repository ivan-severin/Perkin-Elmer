#define WNm_pin 2        // pin of wavenumver
#define pen_pin A0       // pin of analog intensyvity


volatile float wNum = 4000.0;     // wavenumver
volatile float pen = 0.0;



//////////////////////////// Setup //////////////////////////////////////////////////
void setup() {
  Serial.begin(38400);

  pinMode(WNm_pin, INPUT_PULLUP);
  attachInterrupt(0, read_data, FALLING);
  Serial.println("Setup started");
}
///////////////////////////  Main  Loop //////////////////////////////////////////
void loop() {
  //Serial.println('main loop');
  Serial.print(wNum);
  Serial.print('\t');
  Serial.println(pen);
}
////////////////////////// Read data ////////////////////////////////////////////
void read_data() {
  pen = analogRead(pen_pin);
  wNum -= 0.1;

}








