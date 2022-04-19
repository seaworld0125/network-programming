import threading

x = 0

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(300000):
        lock.acquire()
        increment()
        lock.release()

def main_task():
    global x 
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task(lock))
    t2 = threading.Thread(target=thread_task(lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print('t1 complete! ', x)
    print('t2 complete! ', x)

main_task()