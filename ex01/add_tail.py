from helper import Node

def add_tail(list_head, val):
  current = list_head
  while current.next != None:
    current = current.next
  
  current.next = Node(val)

def print_list(list_head):
  current = list_head
  while current != None:
    print(current.content)
    current = current.next

firstHead = Node(3)
secondNode = Node(4)
thirdNode = Node(5)

firstHead.next = secondNode
secondNode.next = thirdNode
add_tail(firstHead, 6)
print_list(firstHead)
