class Node:
	def __init__(self, cargo = None, head= None, next = None):
		self.cargo = cargo
		self.head = head
		self.next = next

	def __str__(self):
		return str(self.cargo)

def print_list(node):
	while node:
		print node,
		node = node.next

def insert_node(node, newnode):
	if node.next == None:
		newnode.head = node
		node.next = newnode
	else:
		oldtail = node.next
		node.next = newnode
		newnode.head = node
		newnode.next = oldtail

def create_list(first, second):
	first.next = second
	second.head = first

def insert_end(first, end):
	if first.next == None:
		first.next= end
		end.head = first
	else:
		insert_end(first.next, end)

def insert_head(first, head):
	first.head = head
	head.next = first

def remove_second(list):
	if list == None: return
	first = list
	second = list.next
	first.next = second.next
	second.next = None
	return second

