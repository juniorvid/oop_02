from helper import Node

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
print_list(firstHead)


