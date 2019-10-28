class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    def set_data(self,data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self,next_ptr):
        self.next = next_ptr
    
    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def set_head(self,head):
        self.head = head

    def list_length(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.get_next()
        
        self.length = count
        return count
    
    def insert_at_beg(self,data):
        new_node = Node()
        new_node.set_data(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1
        
    def insert_at_end(self,data):
        new_node = Node()
        new_node.set_data(data)
        
        current = self.head
        if not current:
            self.head = new_node
        else:
            while current.get_next() != None:
                current = current.get_next()
            
            current.set_next(new_node)
        self.length += 1
    
    def insert_at_pos(self,data,pos):
        if pos < 0 or pos > self.length:
            return None
        else:
            if pos == 0:
                self.insert_at_beg(data)
            elif pos == self.length:
                self.insert_at_end(data)
            else:
                new_node = Node()
                new_node.set_data(data)
                count = 1
                current = self.head
                while count < pos - 1:
                    count += 1
                    current = current.get_next()
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length += 1
    def del_at_beg(self):
        if self.length == 0:
            print("List is empty")
        else:
            temp = self.head
            self.head = self.head.get_next()
            self.length -= 1
            del temp
    def del_at_end(self):
        if self.length == 0:
            print("List is empty")
        else:
            previous_ptr = self.head
            current_ptr = self.head
            while current_ptr.get_next() != None:
                previous_ptr = current_ptr
                current_ptr = current_ptr.get_next()
            
            previous_ptr.set_next(None)
            self.length -= 1
        
    def del_with_node(self,node):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not found in the list")
                else:
                    previous = current
                    current = current.get_next()
                    
            if previous is None:
                # Means the data is in the first node.
                self.head = current.get_next()
                # No need to delete the node as it will be added for garbage collection
            else:
                previous.set_next(current.get_next())
            self.length -= 1
            
    def del_with_value(self,value):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = self.head
            while (current.get_next() != None) and (current.get_data() !=  value):
                previous = current
                current = current.get_next()
            
            if current.get_data() == value:
                previous.set_next(current.get_next())
                self.length -= 1
            else:
                raise ValueError('Value not found in the Linked list.')
                    
    def del_at_pos(self,pos):
        if self.length == 0:
            raise ValueError('The list is empty')
        
        if pos > self.length or pos < 0:
            raise ValueError('Position does not exist in Linked List.')
        else:
            if pos == 0:
                self.head = self.head.get_next()
            else:
                count = 0
                current = self.head
                previous = None
                while (current.get_next() != None) or count < pos:
                    count += 1
                    if count == pos:
                        previous.set_next(current.get_next())
                        self.length -= 1
                        break
                    else:
                        previous = current
                        current = current.get_next()
        
    def traverse(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()


singly_linked_list = LinkedList()
singly_linked_list.insert_at_end(58)
singly_linked_list.insert_at_beg(3)
singly_linked_list.insert_at_beg(4)
singly_linked_list.insert_at_beg(5)
singly_linked_list.insert_at_beg(6)
singly_linked_list.insert_at_end(8)
singly_linked_list.insert_at_pos(82,0)
singly_linked_list.insert_at_pos(83,2)
singly_linked_list.insert_at_pos(84,0)
singly_linked_list.insert_at_pos(85,4)
singly_linked_list.insert_at_pos(86,9)

singly_linked_list.traverse()  
singly_linked_list.del_at_beg()
print("After deleting beginnings node")
singly_linked_list.traverse()
print("After deleting last node")
singly_linked_list.del_at_end()
singly_linked_list.traverse()

print("After deleting 85")
singly_linked_list.del_with_value(85)
singly_linked_list.traverse()
print("After deleting last node.")
singly_linked_list.del_at_pos(8)
singly_linked_list.traverse()