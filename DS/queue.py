"""Circular, fixed size, single ended Queue based on array.

Can insert at the end, remove at the beginning, implemented circularly.
Does not support insertion or removal from the middle.
Overflow or underflow will raise an error.
"""
QUEUE_SIZE = 10

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

    items = [10, 7, 65, 34, None, 98, None, 13, 56, 99, None, None, None, None, None, None, 120, 2342, 4535, 343, 109]
    for item in items:
        if item:
            que.enqueue(item)
        else:
            que.dequeue()
        print(que)

if __name__ == '__main__':
    main()
