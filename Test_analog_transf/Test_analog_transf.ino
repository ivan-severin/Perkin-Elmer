#include <QueueArray.h>

#define WNm_pin 2                  // pin of wavenumver 
//(orange - sig, orange+white -GND)
#define pen_pin A0                 // pin of analog intensyvity (Blue)+
#define scan_pin 4
#define start_pin 5


volatile int wNum = 0;     // wavenumver
volatile int pen = 0;         // relate  Transmiteence
float pen_old = 0.0;
 QueueArray <int> pen_queue;
 QueueArray <int> wnum_queue;
bool s = false;


//////////////////////////// Setup //////////////////////////////////////////////////
void setup() {
  Serial.begin(38400);
  // set the printer of the queue.
    pen_queue.setPrinter (Serial);
   wnum_queue.setPrinter (Serial);
  attachInterrupt(0, read_data, FALLING);
 // pinMode(WNm_pin, INPUT);
  pinMode(scan_pin, INPUT);

  Serial.println("Setup started");
}
///////////////////////////  Main  Loop //////////////////////////////////////////
void loop() {

//  if (! digitalRead(scan_pin)){
//    attachInterrupt(0, read_data, FALLING);
//  }
//  else {
//    detachInterrupt(0);
//  }

  while(!pen_queue.isEmpty () || !wnum_queue.isEmpty ()){
    Serial.print(wnum_queue.pop());
    Serial.print('\t');
    Serial.println(pen_queue.pop());
  }


}


////////////////////////// Read data ////////////////////////////////////////////
void read_data() {
  wNum++;
  pen=analogRead(pen_pin);
  pen_queue.push(pen);
  wnum_queue.push(wNum);
}












