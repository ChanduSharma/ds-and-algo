"""
Reverse level order traversal of binary tree
"""

def reverse_level_order_traversal(root):
    queue = []
    stack = []

    if not root:
        return

    queue.insert(0,root)

    while len(queue) > 0:

        stack.append(queue[-1].data)

        if queue[-1].right:
            queue.insert(0, queue[-1].right)

        if queue[-1].left:
            queue.insert(0, queue[-1].left)

        queue.pop()

    print(*stack[::-1])


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


reverse_level_order_traversal(root)