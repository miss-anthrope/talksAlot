#!/usr/bin/env python
# coding: utf-8
'''
Project 4 - Client 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''
import socket

print("Hey how's it going? I'm Johnny Knoxville and this is a TCP client!")

sock_=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_.connect((socket.gethostname(),8080))
msg=sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))