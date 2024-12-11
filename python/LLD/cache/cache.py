from double_linked_list import DoubleLinkedList, Node

SIZE = 5

class LRUCache:
    recent_items = DoubleLinkedList()
    positions = dict()

    def __init__(self, capacity: int):
        self.capacity = capacity

    def insert(self, value: int):
        """Insert new value in the cache.

        If value pre-exists, pop it from that position and insert at the tail.
        If value doesn't exist, insert at the tail.
        If the cache is at capacity, pop the oldest value first.
        """
        if value in self.positions:
            self.evict_by_node(self.positions[value])
            node = self.recent_items.append(value)
        else:
            if len(self.positions) == self.capacity:
                self.evict_lru()
            node = self.recent_items.append(value)
        self.positions[value] = node

    def evict_lru(self):
        """Takes O(1) time to remove the oldest entry.
        """
        value = self.recent_items.pop()
        self.positions.pop(value)

    def evict_by_node(self, node: Node):
        """Takes O(1) time to remove from the DLL since the pointer to
        the node is readily available.
        """
        self.recent_items.pop_node(node)
        self.positions.pop(node.data)

    def evict_by_value(self, value: int):
        """Takes O(n) time to find the value in the double linked list
        before removing it.
        """
        if value in self.positions:
            self.recent_items.pop_value(value)
            self.positions.pop(value)

    def __str__(self):
        return self.recent_items.__str__()

def main():
    cache = LRUCache(SIZE)
    cache.insert(10)
    cache.insert(75)
    cache.insert(36)
    cache.insert(45)
    cache.insert(23)
    cache.insert(36)
    cache.evict_by_value(10)
    print(cache)

if __name__ == '__main__':
    main()
