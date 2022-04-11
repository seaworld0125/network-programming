import struct
packData = struct.pack('hhI', 1, 2, 3)
print(packData) # 네이티브
print(struct.unpack('hhI', packData))

packData = struct.pack('!hhI', 1, 2, 3)
print(struct.unpack('!hhI', packData))


packData = struct.pack('<hhI', 1, 2, 3) # 리틀 엔디언
print(packData)

packData = struct.pack('>hhI', 1, 2, 3) # 리틀 엔디언
print(packData)

print(struct.calcsize('hhI'))