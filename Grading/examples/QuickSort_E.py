from QueueE import LinkedQueue, Node


def insertion_sort(queue):
    incrementing = queue.head

    while incrementing.next:

        prev = incrementing
        current = incrementing.next
        future = current.next

        if not future or not prev.val > current.val:
            start = queue.head
            while start and start.val < current.val:
                start = start.next

                current = future
                future = future.next

        incrementing = incrementing.next


def pick_pivot(S):
    ''' picks median element of 3 '''
    left_el =  S.head.val
    right_el = S.tail.val
    center_el = S.get_middle()

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

