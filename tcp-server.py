import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

#create the socket to receive the stream
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket into an address
server.bind((bind_ip, bind_port))

#listen 5 connections
server.listen(5)
	
print "[TCPServerLogger] Listening on %s:%d"%(bind_ip, bind_port)

def handleTCPClient(client):
	#print the request sent by client
	request = client.recv(1024)

	print "[TCPServerLogger] Received: %s" % request
	
	#send back a packet -Acknowledge packet
	client.send("ACK!")

while True:

	client, addr = server.accept()

	print "[TCPServerLogger] Accepted connection from %s:%d"%(addr[0], addr[1])
	
	#handle the incomming data
	client_handler = threading.Thread(target=handleTCPClient, args=(client,))
	client_handler.start()
