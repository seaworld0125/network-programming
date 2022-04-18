a = 10
b = a.to_bytes(4, 'big')
print(b)

c = int.from_bytes(b'\x00\x00\x00\x0a', 'big')
c = int.from_bytes(b, 'big')
print(c)