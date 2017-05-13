#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import socket
import subprocess
from appJar import gui # import the library
import threading
sock = socket.socket()
sock.bind((socket.gethostbyname('localhost'), 4545))


def Tagging():
	DIH = open("DeviceInfo.txt", "r+") #Device Info Handler
	DI  = DIH.readlines() #Device Info
	DeviceTag = DI[0]
	EncryptionBool = DI[1]
	MaxBytes = DI[2]
	MSG = "Default Message" # just a test to see if we can display messaged from the parse function
	UI(MSG)
	return DeviceTag, EncryptionBool, MaxBytes
def Connect(sock):
	sock.connect()# server ip adress
	print("Connected to server, entering UI...")
def UI(MSG):
	# top slice - CREATE the GUI
	app = gui()

	### fillings go here ###
	app.addLabel("title", "I suggest we use this... (((appJar)))")
	app.setLabelBg("title", "green")
	app.addTextArea("Server Message")
	app.setTextArea("Server Message", MSG.upper())
	# bottom slice - START the GUI
	app.go()
def Receive():
	Recv = sock.recv(10028)
def Parse(Recv): # under 2024 it is a command from the server,over 2024 but below 10,000 is going to be a direct connection from a nother machine
	Header = sys.getsizeof(Recv)
	if Header <= 2024:
		UI("INCOMING SERVER MESSAGE")
		if Header == "DISCONNECT":
			sock.close()
			sys.exit()
		if Header == "RCV_MSG":
			MSG_SIZE = sock.recv(1024)
			SVR_MSG = sock.recv(MSG_SIZE)
			UI(SVR_MSG)
	# Still going to add the other "headers"
if __name__ == '__main__':
	Tagging()
	
