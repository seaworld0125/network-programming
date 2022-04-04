from collections import deque
from operator import index

data = 'a b c d e'.split(' ')

msg = ''
for d in data[2:]: # msg append
    msg += d

print(msg)