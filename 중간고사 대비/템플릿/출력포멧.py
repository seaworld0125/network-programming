print("abc" * 3)
print("{} and {}".format('You', 'Me'))
print("{0} and {1} are {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'You', b = 'beautiful'))

print("%d" %(3))
print("price : %4.2f" %(654321.1234))
print("price : {0:10.2f}".format(321.1)) # 정수부를 최소 10개 출력하고 부족하면 공백으로 채움, 실수부는 최소 2개 출력

print("price : {0:05d}".format(321)) # 정수부를 최소 5개 출력하고 부족하면 0으로 채움

print("I am %s" % 'taekyoung')
print("I am %x" % 11)
print("I am %o" % 11)