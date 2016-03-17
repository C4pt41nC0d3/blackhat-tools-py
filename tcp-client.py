import socket

thost = "shield.spartantechnologies.org"
tport = 80

#create the socket object like TCP/Socket defined by socket.SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect this tcp client with the host
client.connect((thost, tport))

#send data to the client
client.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%(thost))

#receive data from server
response = client.recv(4096)

print response
