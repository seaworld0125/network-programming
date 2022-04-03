rx_size = 0

while rx_size < data_size:
    data = s.recv(8192)
    if not data:
        break
    rx_size += len(data)

# 수신할 데이터의 크기는 어떻게 알 수 있을까?
#  - 송수신할 데이터의 크기를 미리 약속
#  - 데이터 송신 전 데이터의 크기를 먼저 전송