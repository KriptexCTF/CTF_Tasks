import socket
import threading
from datetime import datetime
from _thread import *
import logging
import sys
from colorama import Fore, Back, Style
import base64

from random import random
import time
import shutil
from colorama import init
from colorama import Fore, Back, Style

def log_write(code, addr):
	time = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
	if(code == -1):
		string = "Server STOPED"
		logging.critical(string)
	elif(code == 0):
		string = f"Connection RESET {addr[0]} {addr[1]}"
		logging.warning(string)
	elif(code == 1):
		string = f"Connection CLOSE {addr[0]} {addr[1]}"
		logging.info(string)
	elif(code == 2):
		string = f"Connection OPEN {addr[0]} {addr[1]}"
		logging.info(string)
	elif(code == 3):
		string = "Server STARTED"
		logging.info(string)
	elif(code == 4):
		string = f"Flag was received {addr[0]} {addr[1]}"
		logging.info(string)
	return time + string

def serv_work(connection, addr):
	limit = 100
	for i in range(limit):
		string = rand_hash()
		a = string.encode("ascii")
		b = base64.b64encode(a)
		c = b.decode("ascii")
		time.sleep(0.1)
		connection.send(str.encode(c + "\n"))
		try:
			connection.send(str.encode(":>> "))
			data = connection.recv(1024)
		except ConnectionResetError as e:
			print(log_write(0, addr))
			connection.close()
			return 0
		if not data:
			break
		if data:
			message = (data.decode("utf-8"))[:-1]
			if(message == 'q'):
				connection.send(str.encode("Connection close!\n"))
				break
			if(message == string):
				connection.send(str.encode("Good\n"))
			else:
				connection.send(str.encode("bad\n"))
				break
	if(i == limit - 1):
		connection.send(str.encode(Fore.GREEN + "Y0u_A7e_$0lVed_Th1s_t@sk\n" + Style.RESET_ALL))
		print(Fore.GREEN + log_write(4, addr) + Style.RESET_ALL)
	print(log_write(1, addr))
	connection.close()

#////////////////////////////
simb = "qwertyuiopasdfghjklzxcvbnm"
numb = "0123456789"
len_hash = 50
#////////////////////////////
def rand(c):
	return (int(random()*100)%c)
def rand_hash():
	random_string = ""
	for i in range(len_hash):
		if(rand(2) == 0):
			random_string += simb[rand(len(simb))]
		else:
			random_string += numb[rand(len(numb))]
	return(random_string)

def get_ip():
	try:
		ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		ip.connect(("8.8.8.8", 80))
		IP = ip.getsockname()[0]
		ip.close()
		return IP
	except Exception:
		return "127.0.0.1"
def MAIN():
	port = 2024
	print(Fore.GREEN + str(get_ip()) + ":" +  str(port) + Style.RESET_ALL)
	sock = socket.socket()
	sock.bind(("", port))
	print(log_write(3, None))
	sock.listen(5)
	while True:
		connection, addr = sock.accept()
		print(log_write(2, addr))
		connection.send(str.encode("You are connected!\nDecode from base64 to ascii 100 times\n"))
		start_new_thread(serv_work, (connection, addr,))
	sock.close()

if __name__ == '__main__':
	filename = (sys.argv[0]).replace(".py", ".log")
	logging.basicConfig(level=logging.INFO, filename=filename,filemode="a+", format="%(asctime)s %(levelname)s %(message)s")
	try:
		MAIN()
	except KeyboardInterrupt:
		print(log_write(-1, None))	
