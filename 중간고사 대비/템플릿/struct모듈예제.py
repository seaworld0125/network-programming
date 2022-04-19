'''
0000 (4bit) = 0 (16진수)
000 (3bit) = 0 (8진수)
0 (1bit) = 0 (2진수)
'''

'''
문자    바이트 순서     크기        정렬
@       네이티브        네이티브    네이티브
=       네이티브        표준        none
<       리틀 엔디언     표준        none
>       빅 엔디언       표준        none
!       네트워크        표준        none
지정안하면 네이티브인듯

포맷    C 타입          Python 타입         표준 크기
c       char            길이가 1인 bytes    1
b       signed char     정수                1
B       unsigned char   정수                1
?       _Bool           bool                1
h       short           정수                2   
H       unsigned short  정수                2
i       int             정수                4     
I       unsigned int    정수                4
l       long            정수                4
L       unsigned long   정수                4
q       long long       정수                8
Q       unsigned long long 정수             8
f       float           float               4
d       double          float               8
s       char[]          bytes               가변
'''

import struct
import binascii
import socket

packed = struct.pack('!H', 27)
print("pack     >> ", packed)
print("binascii >> ", binascii.b2a_hex(packed))

unpacked = struct.unpack('!H', packed)
print("unpack   >> ", unpacked)

packed = struct.pack('!HHI', 17, 64, 3)
print("\npack     >> ", binascii.b2a_hex(packed))
print("\nunpack     >> ", struct.unpack('!HHI', packed))


original = '114.71.220.95'
packed = socket.inet_aton(original)

print('original : ', original)
print('packed : ', binascii.hexlify(packed))
print('unpacked : ', socket.inet_ntoa(packed))