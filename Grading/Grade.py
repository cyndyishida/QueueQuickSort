import QuickSort_Solution as sol_qs
import Queue_Solution as sol_lq
import Queue as stu_lq
import QuickSort as stu_qs

TOTAL = 0

def AddValues(queue, values):
    '''
    :param list: linked list type
    :param fp: file pointer of values
    :return: length of linked list

    add the values from file to list
    '''
    answer = []
    for count, num in enumerate(values):
        queue.enqueue(float(num))
        answer.append(float(num))
    answer.sort()
    return count + 1, answer



def check(answer, queue):
    student = [queue.dequeue() for i in range(len(queue))]
    return student == answer


def run_test(fp):
    '''
    :param fp: file pointer to read in values
    :return: number of right and the length of the linked list

    creates linked lists and runs merge sort, then checks for correct result
    '''
    queue = stu_lq.LinkedQueue()
    count, answer = AddValues(queue,fp)
    stu_qs.quick_sort(queue)

    return check(answer, queue)



'''
UNIT TESTS 
'''
def test1():
    cur_total = 0
    fp = open("testcase01.txt", 'r')
    correct = run_test(fp)
    fp.close()

    global TOTAL
    if correct:
        cur_total = 10
        TOTAL += cur_total
    return f"Testcase 01: {cur_total} / 10"


def test2():
    cur_total = 0
    fp = open("testcase02.txt", 'r')
    try:
        correct = run_test(fp)

        global TOTAL
        if correct:
            cur_total = 10
            TOTAL += cur_total
    except:
        print("Error occured, in test 2, result's in 0")
    fp.close()
    return f"Testcase 02: {cur_total} / 10"



def test3():
    cur_total = 0
    fp = open("testcase03.txt", 'r')
    try:
        correct = run_test(fp)

        global TOTAL
        if correct:
            cur_total = 10
            TOTAL += cur_total
    except:
        print("Error occured, in test 3, result's in 0")
    fp.close()
    return f"Testcase 03: {cur_total} / 10"


def test4():
    cur_total  = 0
    data = [['a','z', 'r', 'c', 'g', 'e', 'a']
        , [1 ,2,4, 5, 3,7]
        , [56,3,5,-22,-4]
        , [12.3, 122, 120.2]
        , [ 1, 2, 3]] 

    for el in range(5):  
        queue = stu_lq.LinkedQueue()
        ans = sol_lq.LinkedQueue()
        for i in data[el] :
            queue.enqueue(i)
            ans.enqueue(i)
        if stu_qs.pick_pivot(queue) == sol_qs.pick_pivot(ans):
            cur_total += 2
            global TOTAL
            TOTAL += 2

    return f"Testcase 04: {cur_total} / 10"


def main():
    print(test1())
    print(test2())
    print(test3())
    print(test4())
    print ("\n\nTotal Score: ", TOTAL )


if __name__ == '__main__':
    main()
