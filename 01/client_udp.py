# coding: utf-8

import socket

target_host, target_port = ("127.0.0.1", 80)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC", (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)
