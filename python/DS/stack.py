"""Stack implemented using an array.

Stack has a fixed upper limit.
"""

SIZE = 10

class Stack:
    stack = []

    def __init__(self, capacity: int):
        self.capacity = capacity
    
    def push(self, value: int):
        if len(self.stack) < self.capacity:
            self.stack.append(value)
        else:
            raise MemoryError("Out of memory")

    def pop(self) -> int:
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            raise MemoryError("Nothing to pop")

    def __str__(self) -> str:
        output = ""
        for value in self.stack[::-1]:
            output += str(value) + " "
        return output

def main():
    s = Stack(SIZE)
    s.push(10)
    s.push(15)
    s.push(13)
    s.push(76)
    s.push(8)
    print(s)
    s.pop()
    s.pop()
    print(s)

if __name__ == '__main__':
    main()
