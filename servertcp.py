#!/usr/bin/python3
# vim: set servertcp.py = <servertcp>:
import socket,os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip='0.0.0.0' #Se colocar um ip específico, terá que o computador esta na rede do ip em questão
port = 881

try:
    server.bind((ip, port))
    server.listen(5)            #Por padrão são 5 conexões
    print('Ouvindo')
    (client_socket, address) = server.accept()
    print('Endereço conectado' + address[0]) #No caso o address é um dupla com ip e porta

    while True:
        res = client_socket.recv(1024)
        print(res.decode())
        msg = input('Digite algo: ') + "\n"
        client_socket.send(msg.encode())

    server.close()

except Exception as error:
    print('Falha: ' + str(error))
    server.close()
