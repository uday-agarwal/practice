'''Typical Process has same interface as a Thread class

Process() to construct a new process
p.start() to start a process
p.join() to wait until the process is terminated

Start methods can be: spawn(), fork(), forkserver()

Communication between processes:
 - Queue: is thread and process safe
 - Pipe: two-way communication
'''

import multiprocessing as mp
import os

def func(name: str, q):
    print(f'hello {name}')
    q.put('first item')
    print(f'process ID: {os.getpid()}')
    print('parent ID: ', os.getppid())

def func2(conn: mp.Pipe):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    mp.set_start_method('spawn') # Setting the default start method
    q = mp.Queue()
    p1 = mp.Process(target=func, args=('uday', q,))
    p1.start()
    print(q.get())
    p1.join()

    parent_conn, child_conn = mp.Pipe()
    p2 = mp.Process(target=func2, args=(child_conn,))
    p2.start()
    print(parent_conn.recv())
    p2.join()
