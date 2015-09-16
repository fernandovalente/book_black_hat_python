# coding: utf-8

import socket
import threading

# PG 27

bind_ip, bind_port = ('0.0.0.0', 9999)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on {0}:{1}".format(bind_ip, bind_port))


# Thrad para tratamento de clients
def handle_client(client_socket):

    # exibe o que for enviado pelo client
    request = client_socket.recv(1024)

    print("[*] Received: {0}".format(request))

    # envia um pacote de volta
    client_socket.send("Hello world!")

    client_socket.close()

while True:
    client, addr = server.accept()
    accept_connection = "[*] Accept connection from: {0}:{1}".format(
        addr[0], addr[1]
    )
    print(accept_connection)

    # Coloca a thread de cliente em ação para tratar os dados de entrada
    client_handler = threading.Thread(
        target=handle_client, args=(client,)
    )
    client_handler.start()
