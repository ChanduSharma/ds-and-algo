class CircularNode:

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

class CircularLinkedList:

	def __init__(self):
		self.head = None


	def display(self):
		if not self.head:
			return

		temp = self.head

		print(temp.get_data())
		temp = temp.get_next()
		while temp != self.head:
			print(temp.get_data())
			temp = temp.get_next()

	def insert_at_beg(self, data):

		new_node = CircularNode()
		new_node.set_data(data)
		new_node.set_next(new_node)
		
		if not self.head:
			self.head = new_node
			return

		new_node.set_next(self.head)

		temp = self.head

		while temp.get_next() != self.head:
			temp = temp.get_next()

		temp.set_next(new_node)
		self.head = new_node

	def insert_at_end(self, data):

		new_node = CircularNode()
		new_node.set_data(data)
		new_node.set_next(new_node)


		if not self.head:
			self.head = new_node
			return

		new_node.set_next(self.head)

		current = self.head

		while current.get_next() != self.head:
			current = current.get_next()

		current.set_next(new_node)

	def del_at_end(self):
		if not self.head:
			return

		current = self.head

		if current.get_next() == current:
			self.head = None
			return

		previous = None
		while current.get_next() != self.head:
			previous = current
			current = current.get_next()

		previous.set_next(current.get_next())
		current = None

	def del_at_beg(self):
		if not self.head:
			return

		current = self.head
		if current.get_next() == current:
			self.head = None
			return

		while current.get_next() != self.head:
			current = current.get_next()

		current.set_next(self.head.get_next())
		self.head = self.head.get_next()




x = CircularLinkedList()
x.insert_at_beg(3)
x.insert_at_beg(2)
x.insert_at_beg(1)
x.insert_at_end(4)

print("Printing the list")
x.display()

print("Delete first node")
x.del_at_beg()
x.display()