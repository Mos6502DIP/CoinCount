import socket
import os
import time
import datetime
from os.path import join
import json
def load(file):
    with open(file+".txt") as d:
        return json.loads(d.read())

def save(name, data):
    with open(name+".txt", "w") as d:
        d.write(json.dumps(data)) # Writes the dictonary to the first line
    print("Data saved!")


Sct=socket.socket()
port = int(input("Custom port number. 89 for defaut:> "))
Sct.bind(("", port))
Sct.listen(100)
print('Started server.')

while True:
    try:
        print("Ready for connection")
        client,add=Sct.accept()
        current_time = datetime.datetime.now()
        print(add , "has connected to server" ,current_time)
        client.send(bytes('Connection Testing', 'utf-8'))
        print(client.recv(1024).decode())
        if client.recv(1024).decode() == "1":
            filename = client.recv(1024).decode()
            client.send(bytes(f"Saving as {filename}", 'utf-8'))
            save(filename, json.loads(client.recv(1024).decode()))
            print(f"Dictonary stored as {filename}")
        else:
            filename = client.recv(1024).decode()
            client.send(bytes(f"Loading as {filename}", 'utf-8'))
            client.send(bytes(json.dumps(load(filename)), 'utf-8'))
            print(f"Loaded stored as {filename}")
        client.close()

    except:
        print("Server Crashed")