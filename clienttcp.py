#!/usr/bin/python3
import socket,os


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #AF_INET = IPV4 e SOCK_STREAM = TCP

ip = "127.0.0.1"
porta = 881

client.connect((ip, porta))

try:
    while True:
        msg = input('Digite algo: ') + "\n"
        client.send(msg.encode())               #No python 3 é necessário utilizar o encode e o decode
        res = client.recv(1048)
        print(res.decode() + '\n')

except Exception as error:
    print ("Falha:"+ str(error))
    client.close()
