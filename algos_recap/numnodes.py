def get_height(root):

    if not root:
        return 0
    
    return 1 + get_height(root.left) + get_height(root.right)
    


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(get_height(root))