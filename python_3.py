#this is python side in which input will give by us for on or off and will get a response from esp32 that desired command is implemented successfully or not.


import serial

ser=serial.Serial('COM1',9600)

while True:
    command=input("Enter either 'ON' OR 'OFF':") #input for esp32
    message=command+"\n"
    ser.write(message.encode()) #sent command to esp32
    print("sent: "+command)

    #response from esp32
    response=ser.readline().decode()
    if response==('LED '+message):
        print("LED "+command+"\n")

    else:
        print("Error/ Invalid command")    



