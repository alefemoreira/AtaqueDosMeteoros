#define motor 13
#define termometro A1

void setup() {
  Serial.begin(9600);
  pinMode(motor, OUTPUT);
}

void loop() {
  //MENUa
  Serial.println("VC QUER :");
  Serial.println("[ a ] Agitar");
  Serial.println("[ b ] Ver calor");

  //delay(5000);
  while (true) {
    if (Serial.available() > 0) {
      lerOpcao(Serial.read());
      break;
    }
  }
  //delay(2000);
}

void lerOpcao(char opcao) {
  switch (opcao) {
    case 'a':
      Serial.println("tempo:");
      ativaAgitador();
      break;

    case 'b':
      Serial.println("\nCalor: ");
      Serial.print(getTemperaturaCelsius(analogRead(termometro)));
      Serial.println(" °C\n");
      break;
  }
  limpaBuffer();
}

float getTemperaturaCelsius(float leitura) {
  return ((leitura / 1024) * 5000) / 10;
}

void ativaAgitador() {
  Serial.println("Agitando\n");
  digitalWrite(motor, HIGH);
  delay(2000);
  digitalWrite(motor, LOW);
}

float getCalorias(float temperatura) {
  float m, c, dt;
  return 0;
}

void limpaBuffer() {
  Serial.end();
  Serial.begin(9600);
}
