from typing import Optional

class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def check_bst(root: Optional[Node]) -> bool:
    if not root:
        return True

    if root.left and root.left.data > root.data:
        return False
    if root.right and root.right.data < root.data:
        return False

    return check_bst(root.left) and check_bst(root.right)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    # root.right.left = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    # Function call
    if check_bst(root) is True:
        print("Is BST")
    else:
        print("Not a BST")
