import socket
import struct
import binascii

class Udphdr:
    format_ = ['!H', '!H', '!H', '!H']

    def __init__(self, srcPort, dstPort, length, checkSum):
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.length = length
        self.checkSum = checkSum
    
    def calc_format_size(self):
        size_ = 0
        for f in self.format_:
            size_ += struct.calcsize(f)
        return size_

    def pack_udphdr(self):
        packed = b''
        packed += struct.pack(self.format_[0], self.srcPort)
        packed += struct.pack(self.format_[1], self.dstPort)
        packed += struct.pack(self.format_[2], self.length)
        packed += struct.pack(self.format_[3], self.checkSum)
        return packed

def unpack_udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8]) # 총 8 바이트
    return unpacked

def getSrcPort(unpacked_ipheader):
    return unpacked_ipheader[0]

def getDstPort(unpacked_ipheader):
    return unpacked_ipheader[1]

def getLength(unpacked_ipheader):
    return unpacked_ipheader[2]

def getCheckSum(unpacked_ipheader):
    return unpacked_ipheader[3]

udphdr = Udphdr(5555, 80, 1000, 65535)
packed_udphdr = udphdr.pack_udphdr()
print(binascii.b2a_hex(packed_udphdr))
print('calc format size :' + str(udphdr.calc_format_size()))

unpacked_udphdr = unpack_udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Src Port: {}\nDst Port: {}\nLength: {}\nChecksum: {}'.format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getCheckSum(unpacked_udphdr)))