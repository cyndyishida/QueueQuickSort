from Queue_Solution import LinkedQueue, Node



def insertion_sort(S):
    ''' sorts queue inplace, returns head of sorted list '''
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
    S.head = helper.next


def pick_pivot(S):
    ''' picks median element of 3 '''
    left_el =  S.head.val
    right_el = S.tail.val
    center_el = S[len(S) // 2 ]

    if center_el < left_el:
        center_el, left_el = left_el, center_el
    if right_el < left_el:
        right_el, left_el = left_el, right_el
    if right_el < center_el :
        right_el , center_el = center_el, right_el

    return center_el


def quick_sort(S):
    ''' sorts list S '''
    n = len(S)
    if n > 10:
        p = pick_pivot(S)
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
        insertion_sort(S)

