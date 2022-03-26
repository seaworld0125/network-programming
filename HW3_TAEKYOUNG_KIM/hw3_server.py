from socket import *
import math

# calculator

# 한계점
# 연산자 우선순위 고려하지 못함
# 계산식 논리 오류를 고려하지 못함
# 과제 요구사항만 충족

def stackToNum(numArr):
    coef = 1
    result = 0

    while numArr:
        result += (numArr.pop() * coef)
        coef *= 10
    return result

def splitMsg(msg):
    opt = ['+', '-', '/', '*']
    opd = []
    splitResult = []

    for c in msg:
        if c in opt:
            if opd:
                splitResult.append(stackToNum(opd))
            splitResult.append(c)
            opd.clear()
        elif c == ' ':
            continue
        else:
            opd.append(int(c))

    splitResult.append(stackToNum(opd))
    return splitResult

def calc(formula):
    opt = ['+', '-', '/', '*']
    curOpt = None
    ans = 0

    for c in formula:
        if c in opt:
            curOpt = c
        else:
            if curOpt:
                if curOpt == '+':
                    ans += c
                elif curOpt == '-':
                    ans -= c
                elif curOpt == '/':
                    ans = math.floor((ans / c) * 10) / 10
                else:
                    ans *= c
            else:
                ans += c
    return ans

# server code

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 2500))
sock.listen(5)

client, addr = sock.accept()
print('connect')

while True:
    try:
        data = client.recv(1024).decode()
    except:
        break
    else:
        if not data or data == 'q':
            print("Connection close")
            break
        print("Received message: ", data)
    
    try:
        formula = splitMsg(data)
        result = calc(formula)
        client.send(str(result).encode())
    except:
        break

client.close()
sock.close()