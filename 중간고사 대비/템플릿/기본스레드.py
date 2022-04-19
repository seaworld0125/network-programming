import threading

def square(num):
    print(num ** 2)

def cube(num):
    print(num ** 3)

t1 = threading.Thread(target=square(4))

t1.start()

t1.join()

print('done')