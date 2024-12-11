from threading import Lock

def main():
    lock = Lock()
    if lock.acquire(blocking=True):
        print('Lock acquired')
    else:
        print('Lock acquisition failed')

    if lock.acquire(blocking=True, timeout=3):
        print('Lock acquired again')
    else:
        print('Lock acquisition failed')

    lock.release()

if __name__ == '__main__':
    main()
