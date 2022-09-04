"""Double linked list.

Provides insertion and deletion at any index.
"""

MAX_SIZE = 4

class Node:
    previous = None
    next = None

    def __init__(self, value: int, previous = None, next = None):
        self.data = value
        self.previous = previous
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, value: int) -> Node:
        """Insert at the tail.
        """
        if self._tail == None:
            self._tail = Node(value)
            self._head = self._tail
        else:
            self._tail.next = Node(value, previous = self._tail)
            self._tail = self._tail.next
        return self._tail

    def pop(self) -> int:
        if self._head == None:
            raise IndexError("Nothing to pop")
        else:
            value = self._head.data
            next = self._head.next
            self._head.next = None
            self._head = next
            if self._head == None:
                self._tail = None
            else:
                self._head.previous = None
            return value

    def pop_node(self, node: Node) -> int:
        if node == None:
            raise ValueError("Bad pointer passed")
        if node == self._head:
            return self.pop()
        elif node == self._tail:
            previous = node.previous
            node.previous = None
            self._tail = previous
            self._tail.next = None
            return node.data
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.previous = None
            node.next = None
            return node.data

    def pop_value(self, value: int) -> int:
        node = self.find(value)
        if node:
            return self.pop_node(node)
        
        return None

    def find(self, value: int) -> Node:
        """Complexity: O(n).

        Requires linear searching.
        """
        ptr = self._head
        while ptr:
            if ptr.data == value:
                return ptr
            ptr = ptr.next
        return None

    def __str__(self):
        output = ""
        ptr = self._head
        while ptr:
            output += "Data:" + str(ptr.data) + ", Previous: " + str(ptr.previous) + ", Next: " + str(ptr.next) + "\n"
            ptr = ptr.next
        return output

def main():
    list = DoubleLinkedList()
    list.append(10)
    list.append(3)
    print(list)
    list.pop()
    print(list)
    test_node = list.append(20)
    list.append(45)
    list.append(16)
    list.append(31)
    list.pop_value(45)
    print(list)
    list.pop_node(test_node)
    print(list)

if __name__ == "__main__":
    main()
