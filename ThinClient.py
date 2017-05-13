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
def Connect(sock):         # mess fix it ^V
	try:
		sock.connect(sock) # server ip adress
	except Exception as e:
		print ('Failed to connect:', e)
		return # sys.os.exit()
	print("Connected to server, entering UI...")
def UI():
	# function called by pressing the buttons
	def press(btn):
	    if btn=="Cancel":
	        app.stop()
	    else:
	        print("User:", app.getEntry('user'), "Pass:", app.getEntry('pass'))

	def regmenu(btn):
		# open a registration menu
		print('(register test look 4 it in the console :)')

	app = gui()

	app=gui("Login Window", "400x200")
	app.setBg("#9BF")
	app.setFont(20)

	app.addLabel("title", "Welcome to appJar", 0, 0, 2)  # Row 0,Column 0,Span 2
	app.addLabel("user", "Username:", 1, 0)              # Row 1,Column 0
	app.addEntry("user", 1, 1)                           # Row 1,Column 1
	app.addLabel("pass", "Password:", 2, 0)              # Row 2,Column 0
	app.addSecretEntry("pass", 2, 1)                     # Row 2,Column 1
	app.addButtons(["Submit", "Cancel"], press, 3, 0, 2) # Row 3,Column 0,Span 2
	app.addLabel("reg", "Don't have an account?", 4, 0, 2)
	app.addButton("Register", regmenu, 5, 0, 2)

	app.setEntryFocus("user")

	app.go()

if __name__ == '__main__':
	Connect(sock)
	UI()
