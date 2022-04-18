import binascii
import socket
addrs = ['114.71.220.95']

for addr in addrs:
    packed = socket.inet_aton(addr)
    print('Original : ', addr)
    print('Packed : ', binascii.hexlify(packed))
    print('Unpacked : ', socket.inet_ntoa(packed))

'''
[네트워크 바이트 순서] : 빅엔디안 (보통 사람이 읽는 순서대로 바이트를 작성함) 

socket.ntohl(x) 4바이트 양의 정수를 네트워크 바이트 순서에서 호스트
                바이트 순서로 변환
socket.ntohs(x) 2바이트 양의 정수를 네트워크 바이트 순서에서 호스트
                바이트 순서로 변환
socket.htonl(x) 4바이트 양의 정수를 호스트 바이트 순서에서 네트워크
                바이트 순서로 변환
socket.htons(x) 2바이트 양의 정수를 호스트 바이트 순서에서 네트워크
                바이트 순서로 변환
'''

a = 1234
htonlA = socket.htonl(a)
ntohlA = socket.ntohl(htonlA)

print(a)
print(htonlA)
print(ntohlA)