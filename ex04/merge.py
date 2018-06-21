from helper import Node

def merge(train1, train2):
  current = train1
  while current.next != None:
    current = current.next
  
  current.next = train2
  return train1

def print_list(list_head):
  current = list_head
  while current != None:
    print(current.content)
    current = current.next
  



train1Head = Node(5)
train1node2 = Node(4)
train1node3 = Node(3)

train1Head.next = train1node2
train1node2.next = train1node3

train2Head = Node(6)
train2node2 = Node(5)
train2node3 = Node(4)

train2Head.next = train2node2
train2node2.next = train2node3

merged = merge(train1Head, train2Head)

print_list(merged)