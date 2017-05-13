import sys
import time
import socket
import subprocess

def Tagging():
	DIH = open("DeviceInfo.txt", "r+") #Device Info Handler
	DI  = DIH.readlines() #Device Info
	DeviceTag = DI[0]
	EncryptionBool = DI[1]
	MaxBytes = DI[2]
	
Tagging()
