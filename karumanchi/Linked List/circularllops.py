class CircularNode:
    __slots__ = ("_data", "_next")

    def __init__(self):
        self._data = None
        self._next = self

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_next(self, next_ptr):
        self._next = next_ptr

    def get_next(self):
        return self._next

class CircularList:

    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.get_data()))
            if current.get_next() is self.head:
                break
            current = current.get_next()
        print("->".join(result))

    def add_at_beg(self, data):
        new_node = CircularNode()
        new_node.set_data(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.set_next(self.head)

            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()

            current.set_next(new_node)
            self.head = new_node
    
    def add_at_end(self, data):
        new_node = CircularNode()
        new_node.set_data(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            current = self.head

            while current.get_next() is not self.head:
                current = current.get_next()
            current.set_next(new_node)
            self.head = new_node
    def del_at_beg(self):
        if not self.head or (self.head.get_next() is self.head):
            self.head = None
        else:
            current = self.head
            while current.get_next() is not self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()

    def del_at_end(self):
        
        if not self.head or (self.head.get_next() is self.head):
            self.head = None
        else:
            temp = self.head
            current = self.head
            while current.get_next() is not self.head:
                temp = current
                current  = current.get_next()

            temp.set_next(self.head)

if __name__ == "__main__":
    x = CircularList()
    x.add_at_beg(3)
    x.add_at_beg(4)
    x.add_at_beg(5)
    x.add_at_beg(6)
    x.add_at_end(2)
    x.display()
    print("After deleting last node")
    x.del_at_end()
    x.display()
