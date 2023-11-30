class Node:
	
	def __init__(self, data):
		
		self.data = data
		self.next = None

# The standard reverse function used
# to reverse a linked list
def reverse(head):

	prev = None
	curr = head

	while (curr):
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	
	return prev

# Function used to reverse a linked list
# from position m to n which uses reverse
# function
def reverseBetween(head, m, n):

	if (m == n):
		return head
		
	# revs and revend is start and end respectively
	# of the portion of the linked list which
	# need to be reversed. revs_prev is previous
	# of starting position and revend_next is next
	# of end of list to be reversed.
	revs = None
	revs_prev = None
	revend = None
	revend_next = None

	# Find values of above pointers.
	i = 1
	curr = head
	
	while (curr and i <= n):
		if (i < m):
			revs_prev = curr

		if (i == m):
			revs = curr

		if (i == n):
			revend = curr
			revend_next = curr.next

		curr = curr.next
		i += 1

	revend.next = None

	# Reverse linked list starting with
	# revs.
	revend = reverse(revs)

	# If starting position was not head
	if (revs_prev):
		revs_prev.next = revend

	# If starting position was head
	else:
		head = revend

	revs.next = revend_next
	return head

def prints(head):

	while (head != None):
		print(head.data, end = ' ')
		head = head.next
		
	print()

# Function to add a new node at the
# beginning of the list
def push(head_ref, new_data):

	new_node = Node(new_data)
	new_node.data = new_data
	new_node.next = (head_ref)
	(head_ref) = new_node
	return head_ref

# Driver code
if __name__=='__main__':
	
	head = None
	head = push(head, 70)
	head = push(head, 60)
	head = push(head, 50)
	head = push(head, 40)
	head = push(head, 30)
	head = push(head, 20)
	head = push(head, 10)
	
	reverseBetween(head, 3, 6)
	
	prints(head)
	
# This code is contributed by rutvik_56
