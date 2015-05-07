class Node:
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)

def game(node):
	while node.next != node:
		turn = 0
		while turn < 2:
			turn += 1
			node = node.next
		secondplace = node
		loser = node.next
		secondplace.next = loser.next
		loser.next = None

		print loser
	
	print "Winner is", node


Allan = Node(1)
Bart = Node(2)
Cassie = Node(3)
Diane = Node(4)

Allan.next = Bart
Bart.next = Cassie
Cassie.next = Diane
Diane.next = Allan

game(Allan)
