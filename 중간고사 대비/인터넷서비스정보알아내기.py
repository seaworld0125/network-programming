import binascii
import socket

print(socket.getservbyport(80))
print(socket.getservbyport(22))

print(socket.getservbyname('http'))
print(socket.getservbyname('https'))