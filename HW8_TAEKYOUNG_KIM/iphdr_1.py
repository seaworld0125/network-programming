import socket
import struct
import binascii

class Iphdr:
    format_ = ['!BBH', '!HH', '!BBH', '!4s', '!4s']

    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45
        self.tos = 0
        self.tot_len = tot_len
        self.id = 0
        self.frag_off = 0
        self.ttl = 127
        self.protocol = protocol
        self.check = 0
        self.saddr = socket.inet_aton(saddr)
        self.daddr = socket.inet_aton(daddr)
    
    def calc_format_size(self):
        size_ = 0
        for f in self.format_:
            size_ += struct.calcsize(f)
        return size_

    def pack_Iphdr(self):
        packed = b''
        packed += struct.pack(self.format_[0], self.ver_len, self.tos, self.tot_len)
        packed += struct.pack(self.format_[1], self.id, self.frag_off)
        packed += struct.pack(self.format_[2], self.ttl, self.protocol, self.check)
        packed += struct.pack(self.format_[3], self.saddr)
        packed += struct.pack(self.format_[4], self.daddr)
        return packed

def unpack_Iphdr(buffer):
    unpacked = struct.unpack('!BBHHHBBH4s4s', buffer[:20]) # 총 20 바이트?
    return unpacked

def getPacketSize(unpacked_ipheader):
    return unpacked_ipheader[2]

def getProtocolId(unpacked_ipheader):
    return unpacked_ipheader[6]

def getIP(unpacked_ipheader):
    src_ip = socket.inet_ntoa(unpacked_ipheader[8])
    dst_ip = socket.inet_ntoa(unpacked_ipheader[9])
    return (src_ip, dst_ip)

ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))
print('calc format size :' + str(ip.calc_format_size()))
print('...')

unpacked_ipheader = unpack_Iphdr(packed_iphdr)
print(unpacked_ipheader)
print('packet size : {}\nProtocol : {}\nIP : {}'.format(getPacketSize(unpacked_ipheader), getProtocolId(unpacked_ipheader), getIP(unpacked_ipheader)))