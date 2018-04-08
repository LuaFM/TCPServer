#!/usr/bin/python3
# vim: set servertcp.py = <servertcp>:
import socket, os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPV4 e SOCK_STREAM = TCP

ip = "0.0.0.0"  # Se colocar um ip específico, o computador deve estar na rede do ip em questão
# Pode ser uma porta a sua escolha
port = int(input("Digite a porta a ser usada pelo server: "))

try:
    server.bind((ip, port))
    server.listen(5)  # Por padrão são 5 conexões
    print("Ouvindo...")
    (client_socket, address) = server.accept()
    # No caso o address é um dupla com ip e porta, o valor 0 se refere ao ip
    print("Endereço conectado - " + address[0])

    while True:
        res = client_socket.recv(1024)
        print(res.decode())
        msg = input('Digite algo: ') + "\n"
        client_socket.send(msg.encode())

    server.close()

except Exception as error:
    print('Falha: ' + str(error))
    server.close()
