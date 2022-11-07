'''While a set can store one entry per element,
a multiset can store count of each element thus
duplicate entries are possible.

A multiset contains:
 - A hashmap for elements and their count

'''

class MultiSet:
    def __init__(self) -> None:
        # Key: element
        # Value: count
        self._multiset = dict()

    def add(self, number: int, count: int = 1) -> None:
        if number in self._multiset:
            self._multiset[number] += count
        else:
            self._multiset[number] = count

    def __str__(self) -> str:
        return str(self._multiset)

def main():
    multiset = MultiSet()
    multiset.add(1, 6)
    multiset.add(1)
    multiset.add(4)
    print(multiset)

if __name__ == '__main__':
    main()