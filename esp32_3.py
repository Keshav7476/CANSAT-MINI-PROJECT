import serial

ser=serial.Serial('COM2',9600)

while True:
    command=ser.readline().decode() #getting response from python
    print("Command Recieved:"+ command)

    #sending response which recieved for confirmation
    if command =='ON\n':
        ser.write('LED ON\n'.encode())

    elif command=='OFF\n':
        ser.write('LED OFF\n'.encode())    

    else:
        ser.write("enter valid command\n".encode())    
        
