#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys

Ip = str(sys.argv[1])
Port = int(sys.argv[2])
Line = ' '.join(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((Ip, Port))
    print("Enviando:", Line)
    my_socket.send(bytes(Line, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
