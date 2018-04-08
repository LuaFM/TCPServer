#!/usr/bin/python3
import socket, os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET = IPV4 e SOCK_STREAM = TCP

# Escolha IP e Porta onde irá levantar o Cliente.
ip = str(input('Informe o IP onde o cliente fará a requisição: '))
porta = int(input('Digite a porta a ser usada pela conexão: '))

client.connect((ip, porta))

try:
    while True:                                 # Para criar uma conexão com chat ou mandar a requisição para o Host
        msg = input('Digite: ') + "\n"
        client.send(msg.encode())               # No python 3 é necessário utilizar o encode e o decode
        res = client.recv(1048)
        print(res.decode() + '\n')

except Exception as error:
    print ("Falha:"+ str(error))
    client.close()
