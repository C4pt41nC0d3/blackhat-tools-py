import socket

thost = "127.0.0.1"
tport = 80

#create the socke
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data to the server
client.sendto("AAABBBCC", (thost, tport))

#receive data from the server
data, addr = client.recvfrom(4096)

print data
