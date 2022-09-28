"""Disjoint set (aka Union find) Data Structure

Operations:
    CreateSet - create initial sets
    Union - merge two sets
    Find - find leader of a set

Key considerations:
    Compressed paths to the leader of a set during find
        This is important to guarantee amortized O(1) find time
    O(m) time to construct disjoint set
    O(1) time to find if two elements are connected
        O(alpha(n)) -> Inverse Ackermann function which is <=4 for most practical n

Check wiki for some differences from the impl here.
"""

class DisjointSet:
    def __init__(self, total_sets: int):
        self.total_sets = total_sets
        self.leaders = {}
        self.ranks = {}
        self.create_sets()

    def create_sets(self) -> None:
        for i in range(self.total_sets):
            self.leaders[i] = i
            self.ranks[i] = 1
    
    def union(self, x: int, y: int) -> None:
        """Combine two elements in one set by making leader of
        one set to be the leader of the other set.
        The set with the larger rank becomes the parent of the 
        other set.
        """
        leader_of_x = self.find(x)
        leader_of_y = self.find(y)
        if leader_of_x == leader_of_y:
            return

        if self.ranks[x] > self.ranks[y]:
            leader_of_y, leader_of_x = leader_of_x, leader_of_y
        
        # X has lower rank than Y
        self.leaders[leader_of_x] = leader_of_y

        # Update rank of the expanded set
        self.ranks[leader_of_y] = self.ranks[leader_of_x] + \
                                  self.ranks[leader_of_y]
        self.total_sets -= 1

    def find(self, element: int) -> int:
        """Find the leader of an element 
        
        1. If it is the element itself, return that.
        2. If not, find the leader and flatten the tree such that
           this element points to the leader directly.
        """
        if self.leaders[element] != element:
            leader = self.find(self.leaders[element])
            self.leaders[element] = leader
            return leader
        
        # There is a better way than recursion for path compression - see wikipedia
        # https://en.wikipedia.org/wiki/Disjoint-set_data_structure

        return element

    def __str__(self) -> str:
        return str(self.leaders)

def main():
    dj = DisjointSet(10)
    print("DJ: ", dj)
    print("Find(1)", dj.find(1))
    print("Find(4)", dj.find(4))
    print("Union(3, 4)", dj.union(3, 4))
    print("Union(3, 4)", dj.union(5, 4))
    print("Union(3, 4)", dj.union(8, 4))
    print("DJ: ", dj)

if __name__ == "__main__":
    main()