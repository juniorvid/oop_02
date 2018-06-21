class Node:
  def __init__(self, content):

    
    self.c = content
    self.n = None

  @property
  def content(self):
    return self.c
  
  @content.setter
  def content(self, val):
    self.c = val
  
  @property
  def next(self):
    return self.n
  
  @next.setter
  def next(self, val):
    self.n = val



class SinglyList:
  def __init__(self):
    self.h = None

  def __iter__(self):
    current = self.head
    while current:
      yield current
      current = current.next
  
  @property
  def head(self):
    return self.h
  
  @head.setter
  def head(self, val):
    self.h = val
  
  def isEmpty(self):
    return self.head == none
  
  def add_head(self, node):
    if self.isEmpty():
      self.head = node
    else:
      node.next = self.head
      self.head = node