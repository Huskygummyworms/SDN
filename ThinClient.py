#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import socket
import subprocess
from appJar import gui # import the library

sock = socket.socket()
sock.bind((socket.gethostbyname('localhost'), 4545))


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
	# top slice - CREATE the GUI
	app = gui()

	### fillings go here ###
	app.addLabel("title", "I suggest we use this... (((appJar)))")
	app.setLabelBg("title", "green")

	# bottom slice - START the GUI
	app.go()

if __name__ == '__main__':
	UI()
