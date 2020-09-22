class DoublyNode:

    __slots__ = ("data","next_ptr","prev_ptr")

    def __init__(self,data,prev_ptr=None,next_ptr=None):
        self.data = data
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr

    def get_data(self):
        return self.data

    def set_next(self,next_ptr):
        self.next_ptr = next_ptr

    def set_prev(self,prev_ptr):
        self.prev_ptr = prev_ptr

    def get_prev(self):
        return self.prev_ptr

    def get_next(self):
        return self.next_ptr

class DoublyLinkedList(object):
    """docstring for DoublyLinkedList"""
    def __init__(self):
        super(DoublyLinkedList, self).__init__()
        self.head = None

    def insert_at_beg(self, data):

        new_node = DoublyNode(data)

        new_node.set_next(self.head)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node

    def insert_at_end(self, data):

        new_node = DoublyNode(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head

        while temp.get_next() is not None:
            temp = temp.get_next()

        temp.set_next(new_node)
        new_node.set_prev(temp)

    def insert_at(self, data, pos):

        assert pos > 0, "Invalid position"
        new_node = DoublyNode(data)

        if pos == 1 or not self.head:
            new_node.set_next(self.head)
            if self.head:
                self.head.set_prev(new_node)

            self.head = new_node
            return


        temp = self.head
        k = 1

        while temp.get_next()  and (k < pos - 1):
            temp = temp.get_next()
            k += 1

        if k != pos-1:
            print('Desired location doesnot exist. Inserting at end')

        new_node.set_next(temp.get_next())
        new_node.set_prev(temp)

        if temp.get_next():
            temp.get_next().set_prev(new_node)

        temp.set_next(new_node)

    def del_at_beg(self):
        if not self.head:
            return

        self.head = self.head.get_next()
        if self.head:
            self.head.set_prev(None)

    def del_at_end(self):

        if not self.head or not self.head.get_next():
            self.head = None
            return

        previous = None
        current = self.head

        while current.get_next():
            previous = current
            current = current.get_next()

        previous.set_next(None)
        current = None

    def del_at(self, pos):

        assert pos > 0, "Invalid Position"

        if not self.head:
            return

        if pos == 1:
            self.head = self.head.get_next()

            if self.head:
                self.head.set_prev(None)
        else:
            k = 1
            current = self.head
            while current.get_next() and k < pos:
                current = current.get_next()
                k += 1

            if k == pos:
                current.get_prev().set_next(current.get_next())
                if current.get_next():
                    current.get_next().set_prev(current.get_prev())



    
    def display(self):
        temp =  self.head

        while temp:
            print(temp.get_data())
            temp = temp.get_next()

    def reverse_display(self, x):
        if not x:
            return

        self.reverse_display(x.get_next())
        print(x.get_data())


x = DoublyLinkedList()
x.insert_at_end(5)
x.insert_at_beg(4)
x.insert_at_beg(3)
x.insert_at_beg(2)
x.insert_at_beg(1)
x.insert_at_end(7)
x.insert_at(6,6)

print("Printing list")
x.display()

x.reverse_display(x.head)
