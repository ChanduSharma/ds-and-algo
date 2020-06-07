class SinglyNode:

    __slots__ = ("_data", "_next")
    def __init__(self):
        self._data = None
        self._next = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_next(self, next_ptr):
        self._next = next_ptr

    def get_next(self):
        return self._next

    def has_next(self):
        return self._next != None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        try:
            new_node = SinglyNode()
            SinglyNode.set_data(new_node, data)
            new_node.set_next(self.head)
            self.head = new_node
        except MemoryError as error:
            print("Could not allocate memory for the node."+ error) 
        

    def insert_at_end(self,data):
        new_node = SinglyNode()
        new_node.set_data(data)

        current = self.head
        if not current:
            self.head = new_node
            return

        while current.has_next():
            current = current.get_next()

        current.set_next(new_node)

    def insert_at(self, data, pos):

        if pos == 1:
            self.insert_at_beg(data)
        else:
            current = self.head
            previous = None
            k = 1
            temp = SinglyNode()
            temp.set_data(data)
            while current and k < pos:
                k += 1
                previous = current
                current = current.get_next()
            previous.set_next(temp)
            temp.set_next(current)

    def del_at_beg(self):
        if not self.head:
            return None
        else:
            temp = self.head
            self.head = temp.get_next()
            temp = None

    def del_at_end(self):

        if not self.head or not self.head.get_next():
            self.head = None
        else:
            previous = None
            current = self.head
            while current.get_next() != None:
                previous = current
                current = current.get_next()

            previous.set_next(None)
            current = None


    def del_at(self, pos):
        """
        To check if the pos exist or not before anything else.
        """

        if not self.head:
            return

        if pos == 1:
            self.head = self.head.get_next()
        else:
            k = 1
            previous = None
            current = self.head
            while current and k < pos:
                k += 1
                previous = current
                current = current.get_next()

            if k == pos:
                previous.set_next(current.get_next())
                current = None

    def del_list(self, method = "iterative"):

        func_dict = {"iterative":self._del_list_iterative}

        func_dict.get(method)()


    def _del_list_iterative(self):

        if not self.head:
            return

        temp = self.head

        while temp:
            self.head = self.head.get_next()
            del temp
            temp = self.head

    def insertion_sort(self):

        if not self.head or not self.head.get_next():
            return

        p = self.head

        while p.get_next():
            q = p.get_next()
            r = q.get_next()
            if q.get_data() < p.get_data():
                temp = self.head
                if q.get_data() < self.head.get_data():
                    q.set_next(self.head)
                    self.head = q
                else:
                    while q.get_data() > temp.get_next().get_data():
                        temp = temp.get_next()

                    q.set_next(temp.get_next())
                    temp.set_next(q)
                p.set_next(r)
            else:
                p = p.get_next()


   
    def display(self):
        temp = self.head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()

x = SinglyLinkedList()
x.insert_at_beg(1)
x.insert_at_beg(2)
x.insert_at_beg(3)
x.insert_at_end(2)
x.insert_at_beg(4)

# x.del_at(4)
print("Printing list")
x.insertion_sort()
x.display()