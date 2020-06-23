class DoubleNode:

    __slots__ = ("_data", "_next","_prev")

    def __init__(self):
        self._data = None
        self._prev = None
        self._next = None
    
    def set_data(self, data):
        self._data = data
    
    def get_data(self):
        return self._data
    
    def set_next(self, next_ptr):
        self._next = next_ptr
    
    def get_next(self):
        return self._next
    
    def set_prev(self, prev_ptr):
        self._prev = prev_ptr
    
    def get_prev(self):
        return self._prev

class DoubleLinkedList:

    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
    
    def insert_at_beg(self, data):
        new_node = DoubleNode()
        new_node.set_data(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
    
    def insert_at_end(self, data):
        new_node = DoubleNode()
        new_node.set_data(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_prev(current)

    def insert_at(self, data, pos):
        
        if pos == 0:
            self.insert_at_beg(data)
        else:

            current = self.head
            new_node = DoubleNode()
            new_node.set_data(data)
            while current and (pos-1) > 0:
                current = current.get_next()
                pos = pos - 1

            if not current:
                print("position does not exist.")
            else:
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                new_node.set_prev(current)
                if new_node.get_next():
                    new_node.get_next().set_prev(new_node)

    def del_at_beg(self):

        if not self.head or not self.head.get_next():
            self.head = None
        else:
            temp = self.head
            self.head = self.head.get_next()
            self.head.set_prev(None)

    def del_at_end(self):

        if not self.head or not self.head.get_next():
            self.head = None
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            previous = current.get_prev()
            current.set_prev(None)
            previous.set_next(None)

    def del_at(self, position):

        if position == 0:
            self.del_at_beg()
        else:
            current = self.head
            while current and (position - 1) > 0:
                current = current.get_next()
                position = position - 1

            if not current:
                print("position does not exist")
            else:
                temp = current.get_next()
                if temp:
                    current.set_next(temp.get_next())
                    if temp.get_next():
                        temp.get_next().set_prev(current)
                    temp.set_next(None)
                    temp.set_prev(None)

if __name__ == "__main__":
    x = DoubleLinkedList()
    x.insert_at_end(2)
    x.insert_at_end(3)
    x.insert_at_end(4)
    x.insert_at(9,2)
    x.display()
    print("deleting")
3   x.del_at(3)
    x.display()
