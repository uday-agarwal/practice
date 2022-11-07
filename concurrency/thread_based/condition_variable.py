from threading import Condition

def main():
    cv = Condition()
    cv.acquire()
    cv.release()
    cv.wait()
    cv.notify_all()

if __name__ == '__main__':
    main()