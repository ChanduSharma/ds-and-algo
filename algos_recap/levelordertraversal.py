def level_order_traversal(root):

    queue = []
    if not root:
        return ''
    
    queue.insert(0, root)

    while len(queue) > 0:
        top = queue[-1]
        print(top.data,"-")

        if top.left:
            queue.insert(0, top.left)
        if top.right:
            queue.insert(0, top.right)
        
        queue.pop()

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    level_order_traversal(root)