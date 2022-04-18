# 예약어 확인하기
import keyword
keyword.kwlist

'''
출력 예시
'''
print("abc" * 3)
print("{} and {}".format('You', 'Me'))
print("{0} and {1} are {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'You', b = 'beautiful'))

print("%d" %(3))
print("price : %4.2f" %(654321.1234))
print("{0:4.2f}".format(654321.1234)) # 정수부는 조절안되는데?

'''
[입력 예시]

n = input("입력해라 쉬ㅂ노마 : ")
print(n)
print(float(n))
print(str(n))
'''

'''
자료형 예시
'''
n = True
print(type(n))

'''
얌마 문자열은 수정안되니까 새로 할당해라!!!
'''
'123'.isdigit() # 문자열이 숫자인가?
'abcABC'.isalpha() # 문자열이 문자인가?
'Ab122'.isalnum() # 문자열이 문자+숫자 혼합인가?
'AB'.isupper() # 문자열이 대문자인가?
'ab'.islower() # 문자열이 소문자인가?
' '.isspace() # 문자열이 공백인가?

str = 'Python programming is easy!'
str.upper() # 대문자로 변환
str.lower() # 소문자로 변환
str.swapcase() # 대소문자 바꾸기
str.title() # 첫 글자만 대문자로 변환

str.count('i') # 문자열에서 'i'의 개수
str.find('o') # 문자열에서 'o'의 처음 위치. 없으면 -1 반환
str.rfind('o') # 문자열에서 'o'가 나오는 가장 나중 위치
str.index('on') # 문자열에서 'on'의 처음 위치. 없으면 ValueError

str.split() # 공백을 기준으로 분리
str.split('b') # 문자열을 ( )속의 문자로 분리

'12'.zfill(5) # 문자열 채우기 (0으로)

print(str.replace('Python', 'test', 6)) # 문자열 치환

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setA > setB) # 부분집합인가

# 가변 매개 변수
def myFunc01(*data):
    sum = 0
    for d in data:
        sum += d
    return sum

# 딕셔너리 매개 변수
def myFunc02(**data):
    pass

sum = lambda x, y : x + y
print(sum(6,4))

num = 5
print(bin(num))
print(oct(num))
print(hex(num))

def P(o):
    print(o)

P('test')