#This program is representing ESP32 sending data to another computer or device with time stamps

import serial
import random
import time
import datetime

ser=serial.Serial('COM1',9600) #connecting to port

while True:
    time_stamp=str(datetime.datetime.now())
    data=str(random.randint(1,100))
    message = "data:"+data+"   time:"+time_stamp+'\n'
    
    ser.write(message.encode()) #sending data to COM2 i.e. computer
    #encoding so that it can send into bytes
    print("Data Sent successfully\n")
    time.sleep(2)  # condition of sending string to reciever every 1 second



