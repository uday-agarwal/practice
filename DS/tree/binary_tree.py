"""Tree

Example binary tree:
        1
       / \
      3   2
     /     \
    5       9
   /       /
  6       7

"""

from collections import deque

class BinaryTree:
    def __init__(self, data: int, left: 'BinaryTree' = None, right: 'BinaryTree' = None):
        self.data = data
        self.left = left
        self.right = right

    def in_order(self):
        if self.left: self.left.in_order()
        print(self.data, end=' ')
        if self.right: self.right.in_order()

    def out_order(self):
        if self.right: self.right.out_order()
        print(self.data, end=' ')
        if self.left: self.left.out_order()

    def pre_order(self):
        print(self.data, end=' ')
        if self.left: self.left.pre_order()
        if self.right: self.right.pre_order()

    def post_order(self):
        if self.left: self.left.post_order()
        if self.right: self.right.post_order()
        print(self.data, end=' ')

    def level_order(self):
        """Is a typical BFS traversal."""
        node_list = deque()
        node_list.append(self)
        while node_list:
            node = node_list.popleft()
            print(node.data, end=' ')
            if node.left: node_list.append(node.left)
            if node.right: node_list.append(node.right)

    def __str__(self):
        return self.in_order()

    def bfs(self):
        return self.level_order()

    def bfs_with_null_entries(self):
        """BFS traversal but each level is separated by Null entries
        in the queue, so any level specific logic can be computed.
        """
        print("BFS with null entries:", end=' ')
        queue = deque()
        queue.append(self)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if not node:
                if queue:
                    queue.append(None)
                continue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def maximum_width(self) -> int:
        """Requires BFS but with a twist. Needs work here."""
        width = 1
        return width

    def longest_path(self):
        """Longest path in the tree.
        For each node - take the max of all children.
        Add the node's value to that and return.
        Involves DFS.
        """
        left_path = 0
        right_path = 0
        if self.left:
            left_path = self.left.longest_path()
        if self.right:
            right_path = self.right.longest_path()
        return max(left_path, right_path) + self.data

    def in_order_iterative(self):
        """Using iteration instead of recursion for DFS
        In order traversal.

        Use a stack. The steps are in a loop:
        Starting state: empty stack, node = root
        1. If node is valid:
            1. Push the node itself to stack.
            2. Node = node.left
        2. If node is not valid:
            1. Pop last node from stack
            2. Process this node.
            3. Node = node.right
        """
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.data, end=' ')
                node = node.right

    def pre_order_iterative(self):
        """Using iteration instead of recursion for DFS
        Pre order traversal.
        """
        # Use a stack and push right first, left later, so that
        # left can be popped first.
        stack = [self]
        while stack:
            node = stack.pop()
            print(node.data, end=' ')
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

def main():
    node6 = BinaryTree(6)
    node5 = BinaryTree(5, node6)
    node3 = BinaryTree(3, node5)
    node7 = BinaryTree(7)
    node9 = BinaryTree(9, node7)
    node2 = BinaryTree(2, None, node9)
    node1 = BinaryTree(1, node3, node2)

    print("In order:", end=' ')
    node1.in_order()
    print('')
    print("In order iterative:", end=' ')
    node1.in_order_iterative()
    print('')
    print("Out order:", end=' ')
    node1.out_order()
    print('')
    print("Pre order:", end=' ')
    node1.pre_order()
    print('')
    print("Pre order iterative:", end=' ')
    node1.pre_order_iterative()
    print('')
    print("Post order:", end=' ')
    node1.post_order()
    print('')
    print("Level order:", end=' ')
    node1.level_order()
    print('')
    print('')
    print("Longest path:", node1.longest_path())
    node1.bfs_with_null_entries()
    print('')
    print("Maximum width: ", node1.maximum_width())

if __name__ == "__main__":
    main()