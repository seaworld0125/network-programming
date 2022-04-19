import threading
import datetime

class myThread(threading.Thread):
    def __init__(self, name, counter):
        super().__init__()
        self.name = name
        self.counter = counter

    def run(self):
        print('\nStarting {}[{}]'.format(self.name, self.counter))
        print_date(self.name, self.counter)
        print('\nExiting {}[{}]'.format(self.name, self.counter))

def print_date(threadName, counter):
    today = datetime.date.today()
    print('\n{}[{}]: {}'.format(threadName, counter, today))

thread1 = myThread('th1', 1)
thread2 = myThread('th2', 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('\nExiting the program')