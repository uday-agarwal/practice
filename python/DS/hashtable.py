"""Hash table implemented as an array.

The hash function is python's inbuilt.
In case of collision, a linked list is used at the index in the array.
"""

SIZE = 10

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __hash__(self):
        return hash((self.first_name, self.last_name))

    def __str__(self):
        return self.first_name

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

class HashEntry:
    def __init__(self, data: Person):
        self.data = data
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.table = [None for _ in range(capacity)]
        self.capacity = capacity

    def insert(self, data: Person):
        index = hash(data) % self.capacity
        entry = HashEntry(data)
        node = self.table[index]
        if not node:
            self.table[index] = entry
        else:
            while node.next:
                node = node.next
            node.next = entry

    def remove(self, data: Person):
        index = hash(data) % self.capacity
        node = self.table[index]
        if node and node.data == data:
            self.table[index] = node.next
            node.next = None
            return
        
        while node and node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next

    def __str__(self):
        output = ""
        for index, entry_list in enumerate(self.table):
            if entry_list:
                output += str(index) + ":"
                while entry_list:
                    output += str(entry_list.data)
                    entry_list = entry_list.next
                    if entry_list:
                        output += "->"
                output += " "
        return output

def main():
    ht = HashTable(SIZE)
    ht.insert(Person("Uday", "Agarwal"))
    ht.insert(Person("Namrata", "Agarwal"))
    ht.insert(Person("Rohit", "Gupta"))
    ht.insert(Person("Kanak", "Verma"))
    ht.insert(Person("Moris", "Boyd"))
    ht.insert(Person("Mishita", "Agarwal"))
    ht.insert(Person("Anand", "Agarwal"))
    print(ht)
    ht.remove(Person("Uday", "Agarwal"))
    print(ht)

if __name__ == '__main__':
    main()
