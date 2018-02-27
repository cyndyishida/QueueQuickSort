class Node:
  """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

  __slots__ = 'val', 'next'         # streamline memory usage

  def __init__(self, val, next):
    self.val = val
    self.next = next

  def __lt__(self, other):
    ''' assumes other is of same type, invoked with "<" '''
    return self.val <= other.val

  def __le__(self, other):
    ''' assumes other is of same type, invoked with "<=" '''
    return self.val <= other.val



class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  def __init__(self):
    """Create an empty queue."""
    self.head = None
    self.tail = None
    self.size = 0


  def __str__(self):
    ''' string implementation of current elements in queue '''
    head = self.head
    values = list()
    while head:
      values.append(str(head.val))
      head = head.next

    return ", ".join(values)

  __repr__ = __str__


################## start modifying below this line ######################
  def __len__(self):
    pass

  def is_empty(self):
    pass

  def dequeue(self):
    pass


  def enqueue(self, element):
    pass


  def __getitem__(self,index):
    pass

