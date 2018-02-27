from linked_queue import LinkedQueue, Node


def insertion_sort(S):
    helper = Node(0,None)
    cur = S.head
    pre = helper
    next = None
    while cur:
        next = cur.next
        while pre.next and pre.next < cur :
            pre = pre.next
        cur.next = pre.next
        pre.next = cur
        pre = helper
        cur = next
    return helper.next


def swap( A, B):
    A.val, B.val = B.val, A.val


def pick_pivot(S, left, right):
    center = (left + right) // 2
    left_el = S[left]
    right_el = S[right]
    center_el = S[center]

    if center_el < left_el:
        swap(left_el, center_el)
    if right_el < left_el:
        swap(right_el, left_el)
    if right_el < center_el :
        swap(center_el, right_el)

    last_el = S[right - 1]
    swap (center_el, last_el)
    return last_el.val


def quick_sort(S):
    n = len(S)
    if n >= 11:
        p = pick_pivot(S,0, n -1 )
        L = LinkedQueue()
        E = LinkedQueue()
        G = LinkedQueue()
        while not S.is_empty():
            initial = S.head.val
            if initial< p:
                L.enqueue(S.dequeue())
            elif p < initial:
                G.enqueue(S.dequeue())
            else:
                E.enqueue(S.dequeue())
        quick_sort(L)
        quick_sort(G)
        while not L.is_empty():
            S.enqueue(L.dequeue())
        while not E.is_empty():
            S.enqueue(E.dequeue())
        while not G.is_empty():
            S.enqueue(G.dequeue())
    else:
        S.head = insertion_sort(S)


A= [1,7,5, 9, 7,3, 4,10 ,1 ,2,0 ,1,7,7,8 ]
data=LinkedQueue() #queue object
for i in range(len(A)):
    data.enqueue(A[i])

quick_sort(data)
