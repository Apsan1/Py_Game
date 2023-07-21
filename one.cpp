// C++ code
// done by Apsan Rana Magar
int led1 = 13; // the pin the LED is attached to
int led2 = 12; // the pin the LED is attached to
int led3 = 11; // the pin the LED is attached to
int led4 = 10; // the pin the LED is attached to
void setup()
{
  pinMode(led1, OUTPUT);
	pinMode(led2, OUTPUT);
	pinMode(led3, OUTPUT);
	pinMode(led4, OUTPUT);
}

void loop() {
  // creating a binary converting equation where each 1
  //would light up the led
for (int k = 0; k < 16; k++)
    {
        printf("%d \n", k);
    
     //number to be converted
    int binary[8];//it can inculde 8 bits
    int i = 0; //initialized i for the for loop
  	while (n > 0){ // creating a loop
        binary[i] = n % 2;//it will store the remainder of n/2 in binary array
        n = n / 2;//it will divide n by 2
        i++;//it will increment i by 1
    }
    for (int j = i - 1; j >= 0; j--){//it will print the binary number
        printf("%d", binary[j]);
    }
    printf("\n");
}
//Apsan
}