'''Threads in python are good for I/O bound tasks
not for CPU bound.

Thread() invokes constructor
t.start() starts a thread
t.join() makes the caller wait for the thread to finish before proceeding
'''

from time import perf_counter, sleep
from threading import Thread

def hello(count: int, name: str):
    print(f'Hello {name} times {count}')
    sleep(1)
    print('Done')

def main():
    t1 = Thread(target=hello, name='Hello World', args=(1, 'Uday'))
    t2 = Thread(target=hello, name='Hi there', args=(1, 'Uday'))

    start_time = perf_counter()
    t1.start()
    t2.start()

    print('Threads started')
    t1.join()
    t2.join()
    end_time = perf_counter()
    print(f'Total time: {end_time - start_time}')

if __name__ == '__main__':
    main()
