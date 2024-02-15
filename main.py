#Includes
import serial
from datetime import date

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    #print_hi('PyCharm')
    #ser = serial.Serial(port='COM3', baudrate=9600)
    ser = "Yup"
    today = date.today()
    #while (1):
        #value = ser.readline()
        #valueInString = str(value, 'UTF-8')
    valueInString = "Sheeesh"
    print(today)
    if (valueInString != ""):  # Vérifier ce qu'on recoit vraiment
        f = open("../Raw data/"+str(today)+".txt", "x")
        f.write("" + valueInString)
        f.close()