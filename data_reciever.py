#This program is getting data from ESP32 and getting stored in CSV file through file handling

import serial
import csv


ser=serial.Serial('COM2',9600) #connecting to port
while True:
    with open("cansatdata.csv", mode="a", newline="") as file:
    #a stands for appending and it created file cansatdata.csv if not exsited earlier    
        writer = csv.writer(file) #creates a writer object that you will use to write data.
        line=ser.readline().decode() #bytes to string
        print(str(line))
        writer.writerow([line]) #allow to write data recieved in the file (cansatdata.csv)
    

