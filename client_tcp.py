# coding: utf-8

import socket

target_host, target_port = ("www.google.com", 80)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4696)

print(response)

