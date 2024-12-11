'''Pool of worker processes that can be offloaded tasks


'''

import multiprocessing as mp
import os
import time

def func(x):
    print(f'Process: {os.getpid()}, Parent: {os.getppid()}')
    return x*x

if __name__ == "__main__":
    print(mp.cpu_count())
    
    with mp.Pool(processes=5) as pool:
        print(pool.map(func, [1, 2, 3]))
        output = pool.apply_async(time.sleep, (15, ))
        try:
            print(output.get(timeout=20))
        except mp.TimeoutError:
            print('TimeoutError occured. The process with sleep hasn\'t returned yet.')

        result = pool.apply_async(func, (5, ))
        print(result.get(timeout = 1))
    
