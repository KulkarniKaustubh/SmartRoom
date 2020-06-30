int led = 13;
int ret_val;

void setup()
{
  Serial.begin(9600);
  pinMode (led, OUTPUT);
  digitalWrite (led, LOW);
  Serial.println("Initialising board");
}

void loop()
{
  while (Serial.available()) {
    ret_val = Serial.read();
  }
  
  if (ret_val == '1') {
//  Serial.println("Lighting up LED");
    digitalWrite (led, HIGH);
  } else if (ret_val == '0') {
    digitalWrite (led, LOW);
  }
}
