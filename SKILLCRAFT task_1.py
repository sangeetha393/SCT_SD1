def Kelvin():
    Celsius = float(input("Enter temperature in Celsius: "))
    Kelvin = Celsius+273.15
    print("The temperature in Kelvin is: ",Kelvin)

def Celsius():
    Kelvin = float(input("Enter temperature in Kelvin: "))
    Celsius = Kelvin-273.15
    print("The temperature in Celsius is: ",Celsius)
    
def Fahrenheit_to_kelvin():
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Kelvin = (Fahrenheit-273.15)/1.8 + 273.15
    print("The temperature in Kelvin is: ",Kelvin)

def Kelvin_to_fahrenheit():
    Kelvin = float(input("Enter temperature in Kelvin: "))
    Fahrenheit = (Kelvin - 273.15)*1.8 + 32
    print("The temperature in Fahrenheit is: ",Fahrenheit)
    
def ():
    Celsius = float(input("Enter temperature in Celsius: "))
    Fahrenheit = (Celsius*1.8)+32
    print("The temperature in Fahrenheit is: ",Fahrenheit)
    
def Fahrenheit_to_celsius():
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = (Fahrenheit-32)/1.8
    print("The temperature in Celsius is: ",Celsius)
    
def main():
    print("hello welcome ")
    print("Temperature Converter")
    print(''' 
    1.To convert Celsius to Kelvin.
    2.To convert Kelvin to Celsius.
    3.To convert Fahrenheit to Kelvin.
    4.To convert Kelvin to Fahrenheit.
    5. To convert Celsius to Fahrenheit.
    6.To convert Fahrenheit to celsius.
    ''')
    choice = input("Enter your choice: ")
    if(choice=='1'):
        Kelvin()
    
    elif(choice=='2'):
        Celsius()

    elif(choice=='3'):
        Fahrenheit_to_kelvin()
    
   
    elif(choice=='4'):
        Kelvin_to_fahrenheit()

    elif(choice=='5'):
        Celsius_to_fahrenheit()

    elif(choice=='6'):
        Fahrenheit_to_celsius()

    else:
        print("Invalid choice!!!")

main()