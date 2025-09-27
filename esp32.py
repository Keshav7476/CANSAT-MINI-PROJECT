#its a sender part. COM1 will send some prompt from here and connected port can access the prompts


import serial
import time

# COM port of the sender 
SERIAL_PORT = "COM1"

ser = serial.Serial(SERIAL_PORT, 9600) #opening and connecting to the port
print("Sending data to " + SERIAL_PORT)

while True:
    message = "Hello, Cansat!\n"
    ser.write(message.encode())
    #encoding so that it can send into bytes
    print("Data Sent sucessfully\n")
    time.sleep(1)  # condition of sending string to reciever every 1 second

