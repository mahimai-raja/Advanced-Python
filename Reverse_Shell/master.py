import time 
import socket 
import sys
import os

host = socket.gethostname()
port = 1234              # Simply specify an open port 

s = socket.socket()
s.bind((host, port))
s.listen()

conn, addr = s.accept()
print(f'IP of connected computer : {addr}')

while True :
    command = input(str("Enter a command :- "))
    conn.send(command.encode())
    print(f'Command : {command} has sent')
    if command == 'quit()':
        print(" --- End of Execution --- ")
        break

    data = conn.recv(1024)
    if data :
        print(f"Received : \n {data} ")