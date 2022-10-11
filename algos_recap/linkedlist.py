class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def traversal(self):

        first = self.head

        while first:
            print(first.data)
            first = first.next

family = LinkedList()
family.head = Node("Dady")
wife = Node("Mummy")
first_kid = Node("Tondu")
second_kid = Node("Thappu")
third_kid = Node("khopadi")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid
second_kid.next = third_kid

family.traversal()