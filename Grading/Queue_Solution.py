class Node:
  """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

  __slots__ = 'val', 'next'         # streamline memory usage

  def __init__(self, val, next):
    self.val = val
    self.next = next

  def __lt__(self, other):
    return self.val <= other.val

  def __le__(self, other):
    return self.val <= other.val



class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  def __init__(self):
    """Create an empty queue."""
    self.head = None
    self.tail = None
    self.size = 0


  def __str__(self):
    head = self.head
    values = list()
    while head:
      values.append(str(head.val))
      head = head.next

    return ", ".join(values)

  __repr__ = __str__


################## start modifying ######################
  def __len__(self):
    """Return the number of elements in the queue."""
    return self.size


  def is_empty(self):
    """Return True if the queue is empty."""
    return self.size == 0


  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).
    """

    answer = self.head.val
    self.head = self.head.next
    self.size -= 1
    if self.is_empty():                     # special case as queue is empty
      self.tail = None                     # removed head had been the tail
    return answer



  def enqueue(self, element):
    """Add an element to the back of queue."""
    newest = Node(element, None)            # node will be new tail node
    if self.is_empty():
      self.head = newest                   # special case: previously empty
    else:
      self.tail.next = newest
    self.tail = newest                     # update reference to tail node
    self.size += 1



  def __getitem__(self,index):
    curr = self.head
    for i in range(index):
      curr = curr.next
    return curr.val


