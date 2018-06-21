from helper import Node

def has_cycle(list_head):
  current = list_head
  while current.next != None:
    if current.next == list_head:
      return True
      break
    else:
      current = current.next


  return False
  



firstHead = Node(3)
secondNode = Node(4)
thirdNode = Node(5)

firstHead.next = secondNode
secondNode.next = thirdNode
thirdNode.next = firstHead
print(has_cycle(firstHead))
