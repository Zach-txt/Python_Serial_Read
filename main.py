#Includes
import sys

import serial
from datetime import date

ser = serial.Serial(port='COM2', baudrate=9600)
today = date.today()

while(1):
    value= ser.readline()
    valueInString =str(value, 'UTF-8')
    print(valueInString)

    if(valueInString != ""):#Vérifier ce qu'on recoit vraiment
        f = open("C:\Ecole\PMC\S7\Serial Read\Raw data/" + today, "a")
        f.write(""+valueInString)
        f.close()

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



#if __name__ == '__main__':
    #print_hi('PyCharm')


