#!/usr/bin/python3
# coding=utf-8

def k_largest(A, k):
    #print(A)
    if k == 0:
        return []
    n = len(A)
    B = [A[i] for i in range(k)] # B for Best!
    for i in range(1, k):
        temp = B[i]
        if B[i] < B[i-1]:
            B[i] = B[i-1]
            B[i-1] = temp
    
    for i in range(k, n):
        v = 0
        temp = B[v]
        while v+1 < k and B[v] < A[i]:
            B[v] = A[i]
            v += 1
        print(v, i)
        
        while v >= 0:
            B[v] = A[i]
            temp, B[v-1] = B[v-1], temp
            v -=1

    return B        
    



# Sett med tester.
tests = [
    (([], 0), []),
    (([1], 0), []),
    (([1], 1), [1]),
    (([1, 2], 1), [2]),
    (([-1, -2], 1), [-1]),
    (([-1, -2, 3], 2), [-1, 3]),
    (([1, 2, 3], 2), [2, 3]),
    (([3, 2, 1], 2), [2, 3]),
    (([3, 3, 3, 3], 2), [3, 3]),
    (([4, 1, 3, 2, 3], 2), [3, 4]),
    (([4, 5, 1, 3, 2, 3], 4), [3, 3, 4, 5]),
    (([9, 3, 6, 1, 7, 3, 4, 5], 4), [5, 6, 7, 9]),
]

for test, solution in tests:
    student_answer = k_largest(*test)
    if type(student_answer) != list:
        print("Metoden må returnere en liste")
    else:
        student_answer.sort()
        if student_answer != solution:
            print(
                "Feilet for testen {:}, resulterte i listen ".format(test)
                + "{:} i stedet for {:}.".format(student_answer, solution)
            )