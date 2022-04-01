#!/usr/bin/env python
# coding: utf-8
'''
Project 4 - Server 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''
import socket

print("Hey how's it going? I'm Johnny Knoxville and this is a TCP server!")

host=socket.gethostname()
port=8080

sock_=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.bind((host,port))
sock_.listen(1)

print("\nServer started...\n")


conn,addr=sock_.accept()

print("Connection established with: ",str(addr))

message="\nThanks for your connection "+str(addr)
conn.send(message.encode("ascii"))
conn.close()
