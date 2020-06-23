class SinglyNode:
    __slots__ = ("data","_next")

    def __init__(self):
        self.data = None
        self._next = None
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self, next_node):
        self._next = next_node
    
    def get_next(self):
        return self._next

class SinglyList:

    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
    
    def add_at_beg(self,data):
        try:
            node = SinglyNode()
            node.set_data(data)
            node.set_next(self.head)
            self.head = node
        except MemoryError as error:
            print("Could not add node because "+ error)
    
    def add_at_end(self,data):
        if not self.head:
            self.add_at_beg(data)
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()

            node = SinglyNode()
            node.set_data(data)
            current.set_next(node)
    
    def add_at_pos(self, data, pos):

        if pos == 0:
            self.add_at_beg(data)
        else:
            node = SinglyNode()
            node.set_data(data)

            current = self.head
            while current and (pos - 1) > 0:
                pos = pos - 1
                current = current.get_next()
            
            if not current:
                print("position does not exist.")
            else:
                node.set_next(current.get_next())
                current.set_next(node)

    def del_at_beg(self):
        if not self.head:
            return None
        else:
            temp = self.head
            self.head = temp.get_next()
            return temp
    
    def del_at_end(self):

        if not self.head or not self.head.get_next():
            self.head = None
            return None
        else:
            current = self.head
            prev = self.head

            while current.get_next():
                prev = current
                current = current.get_next()

            prev.set_next(None)
            return current
    
    def del_at_pos(self, position):

        if not self.head:
            raise("List Empty")
        else:
            if position == 0:
                temp = self.head
                self.head = self.head.get_next()
                return temp
            else:

                count = 0
                current = self.head

                while current and count < (position - 1):
                    count += 1
                    current = current.get_next()
                
                if not current and not current.get_next():
                    return None
                
                temp = current.get_next()
                current.set_next(temp.get_next())
                temp.set_next(None)
                return temp


if __name__ == "__main__":
    x = SinglyList()
    # x.add_at_beg(2)
    # x.add_at_beg(4)
    # x.add_at_end(4)
    # x.add_at_pos(3,0)
    x.del_at_pos(0)
    x.display()
