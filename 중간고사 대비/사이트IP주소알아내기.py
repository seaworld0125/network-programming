import socket

HOSTS = [
    'www.sch.ac.kr',
    'homepage.sch.ac.kr',
    'www.daum.net',
    'www.google.com',
    'iot'
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except Exception as e:
        print('{} : {}'.format(host, str(e)))