import QuickSort_E as QS
import QueueE as Q




x = Q.LinkedQueue()
x.enqueue(0)
x.enqueue(2)
x.enqueue(1)
x.enqueue(3)
print(x)

QS.insertion_sort(x)
print(x)
