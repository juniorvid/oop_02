from helper import Node



def sort_asc(unsorted_list):
  if (unsorted_list == None or unsorted_list.next == None):
	  return unsorted_list
  
  middle = get_middle(unsorted_list)
  right = middle.next
  middle.next = None

  print('left')
  print_list(unsorted_list)
  print('right')
  print_list(right)

  sortedLeft = sort_asc(unsorted_list)
  sortedRight = sort_asc(right)

  sortedList = sorted_merge(sortedLeft, sortedRight)
  return sortedList

def sorted_merge(left, right):
  result = None
  if left == None:
    return right
  if right == None:
    return left
  
  if left.content <= right.content:
    result = left
    result.next = sorted_merge(left.next, right)
  
  else:
    result = right
    result.next = sorted_merge(left, right.next)

  print('Result')
  print(result)
  return result



def get_middle(unsorted_list):
  fast = unsorted_list.next
  slow = unsorted_list

  while fast != None:
    fast = fast.next
    if fast != None:
      slow = slow.next
      fast = fast.next
  
  return slow

  
def print_list(list_head):
  current = list_head
  while current != None:
    print(current.content)
    current = current.next
  

def merge(train1, train2):
  current = train1
  while current.next != None:
    current = current.next
  
  current.next = train2
  return train1



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
final = sort_asc(merged)

print_list(final)