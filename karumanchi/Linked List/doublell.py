class DoubleNode:

    def __init__(self):
        self.data = None
        self._next = None
        self._prev = None
    
    def set_data(self, data):
        self._data = data
    
    def get_data(self):
        return self._data

    def set_next(self, next_ptr):
        self._next = next_ptr
    
    def set_prev(self, prev_ptr):
        self._prev = prev_ptr
    
    def get_next(self):
        return self._next
    
    def get_prev(self):
        return self._prev
    
    def has_next(self):
        return self._next != None

class DoubleList:

    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        data = []
        while current:
            list.append(data, str(current.get_data()))
            current = current.get_next()
        
        print("->".join(data))
    

    def display_rev(self):
        current = self.head
        data = []
        while current.get_next():
            current = current.get_next()
        
        while current:
            data.append(str(current.get_data()))
            current = current.get_prev()            
        
        print("->".join(data))

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
            currrent_node = self.head
            while currrent_node.get_next():
                currrent_node = currrent_node.get_next()
            currrent_node.set_next(new_node)
            new_node.set_prev(currrent_node)

    def insert_at_pos(self, data, loc):

        if loc == 0:
            self.insert_at_beg(data)
        else:
            currrent_node = self.head
            count = 0
            while currrent_node and count < loc:
                count +=1
                currrent_node = currrent_node.get_next()

            previous_node = currrent_node.get_prev()
            new_node = DoubleNode()
            new_node.set_data(data)
            new_node.set_prev(previous_node)
            new_node.set_next(currrent_node)
            previous_node.set_next(new_node)


    
if __name__ == "__main__":
    x = DoubleList()    
    x.insert_at_beg(1)
    x.insert_at_beg(2)
    x.insert_at_beg(3)
    x.insert_at_beg(4)
    x.insert_at_beg(5)
    x.insert_at_end(6)
    x.insert_at_end(7)
    x.insert_at_end(8)
    x.insert_at_end(9)
    x.insert_at_pos(10, 2)
    x.display()
    x.display_rev()