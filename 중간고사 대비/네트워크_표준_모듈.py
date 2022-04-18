import ipaddress

def P(o):
    print(o)

addr4 = ipaddress.ip_address('192.0.2.1')
P(addr4)
P(addr4.version)

addr6 = ipaddress.ip_address('2001:A8::1')
P(addr6)
P(addr6.version)

net = ipaddress.ip_network('114.71.220.0/24')
P(net.with_netmask)
P(net.num_addresses)
P(net.netmask)
P(net.hostmask)

import socket

P(socket.gethostname())
P(socket.gethostbyname(socket.gethostname()))

P(socket.gethostbyname_ex('homepage.sch.ac.kr'))

P(socket.getfqdn('220.69.189.98'))