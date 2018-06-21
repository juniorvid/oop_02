from helper import Node

def remove(list_head, val):
  current = list_head
  while current.next != None:
    if current.next.content == val:
      current.next = current.next.next
      return
    else:
      current = current.next

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
remove(firstHead, 4)
print_list(firstHead)
