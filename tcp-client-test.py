import socket

thost = "0.0.0.0"
tport = 9999

#create the socket object like TCP/Socket defined by socket.SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect this tcp client with the host
client.connect((thost, tport))

#send data to the client
client.send("\r\niZZZZ\r\n")

#receive data from server
response = client.recv(4096)

print response
