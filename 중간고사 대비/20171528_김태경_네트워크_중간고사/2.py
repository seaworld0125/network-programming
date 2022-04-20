import string
from typing import List
from xml.etree.ElementTree import tostring, tostringlist


lst = ['H', 'e', 'l', 'l', 'o', ' ', 'I', 'a', 'T']

#A
lst[7] = 'o'
print(lst)

#B
lst.append('?')
print(lst)

#C
print(len(lst))

#D
print(''.join(lst))

#E
lst.sort()
print(lst)