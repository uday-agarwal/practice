"""Circular, fixed size, single ended Queue based on array.

Can insert at the end, remove at the beginning, implemented circularly.
Does not support insertion or removal from the middle.
Overflow or underflow will raise an error.
"""
QUEUE_SIZE = 5

class Queue:
    def __init__(self, capacity: int):
        self._q = [None for _ in range(capacity)]
        self._capacity = capacity
        self._size = 0
        self._head = 0
        self._tail = 0

    def enqueue(self, item: int):
        if self._size < self._capacity:
            self._q[self._tail] = item
            self._tail += 1
            self._tail %= self._capacity
            self._size += 1
        else:
            raise OverflowError("Queue is full")

    def dequeue(self) -> int:
        if self._size > 0:
            value = self._q[self._head]
            self._q[self._head] = None
            self._head += 1
            self._head %= self._capacity
            self._size -= 1
            return value
        else:
            raise IndexError("Queue is empty")

    def __str__(self):
        output = ""
        for i in range(self._head, self._head + self._size):
            output += str(self._q[i % self._capacity]) + " "
        return output

def main():
    que = Queue(QUEUE_SIZE)
    que.enqueue(10)
    print(que)
    que.enqueue(7)
    print(que)
    que.enqueue(65)
    print(que)
    que.enqueue(34)
    print(que)
    que.dequeue()
    print(que)
    que.enqueue(98)
    print(que)
    que.dequeue()
    print(que)
    que.enqueue(13)
    print(que)
    que.enqueue(56)
    print(que)
    que.enqueue(99)
    print(que)
    que.dequeue()
    print(que)
    que.dequeue()
    print(que)
    que.dequeue()
    print(que)
    que.dequeue()
    print(que)
    que.dequeue()
    print(que)
    que.enqueue(120)
    print(que)
    que.enqueue(2342)
    print(que)
    que.enqueue(4535)
    print(que)
    que.enqueue(343)
    print(que)
    que.enqueue(109)
    print(que)

if __name__ == '__main__':
    main()
