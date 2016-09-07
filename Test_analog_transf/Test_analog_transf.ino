#include <QueueArray.h>

#define WNm_pin 2                  // pin of wavenumver 
//(orange - sig, orange+white -GND)
#define pen_pin A0                 // pin of analog intensyvity (Blue)+
#define scan_pin 4
#define start_pin 5


volatile float wNum = 4000.0;     // wavenumver
volatile float pen = 0.0;         // relate  Transmiteence
float pen_old = 0.0;
QueueArray <float> pen_queue;
QueueArray <float> wnum_queue;
bool scan = false;
bool s = false;

//////////////////////////// Setup //////////////////////////////////////////////////
void setup() {
  Serial.begin(38400);
  // set the printer of the queue.
  pen_queue.setPrinter (Serial);
  wnum_queue.setPrinter (Serial);
  //attachInterrupt(0, read_data, RISING);
  pinMode(WNm_pin, INPUT_PULLUP);
  //pinMode(scan_pin, INPUT);

  Serial.println("Setup started");
}
///////////////////////////  Main  Loop //////////////////////////////////////////
void loop() {
  s = !digitalRead(scan_pin);
  if (s ){
    if (! scan){ 
      attachInterrupt(0, read_data, FALLING);
      Serial.println("attachInterrupt");
    }
    scan = true;
    
  }
  else {
    detachInterrupt(0);
    Serial.println("detachInterrupt");
  }

  if( !pen_queue.isEmpty() ){
    Serial.print(wnum_queue.pop());
    Serial.print('\t');
    Serial.println(pen_queue.pop());
  }


}


////////////////////////// Read data ////////////////////////////////////////////
void read_data() {
  wNum -= 0.1;
  pen=analogRead(pen_pin);
  pen_queue.push(pen);
  wnum_queue.push(wNum);
}













