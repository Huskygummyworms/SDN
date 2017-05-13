import sys
import time
import socket
import subprocess

sock = socket.socket()
sock.bind(sock.gethostbyname(), 4545)





def Tagging():
	DIH = open("DeviceInfo.txt", "r+") #Device Info Handler
	DI  = DIH.readlines() #Device Info
	DeviceTag = DI[0]
	EncryptionBool = DI[1]
	MaxBytes = DI[2]
	return DeviceTag, EncryptionBool, MaxBytes
def Connect(sock):
	sock.connect()# server ip adress
	print("Connected to server, entering UI...")
def UI():
	
	
