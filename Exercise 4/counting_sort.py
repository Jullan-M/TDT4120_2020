#!/usr/bin/python3
# coding=utf-8


def counting_sort(A, B):
    n = len(A)

    C = [0 for i in range(2048)]
    # Count every integer from 0 to 2048
    for i in range(n):
        C[A[i]] += 1
    
    # Cumulative sum of integer counts from 0 to 2048
    for j in range(1, 2048):
        C[j] += C[j-1]
    
    # The sorting loop
    for k in range(n-1, -1, -1):
        C[A[k]] -= 1 # This comes before the sorting because python uses 0-indexed lists (as opposed 1-indexed as in the book)
        B[C[A[k]]] = A[k]
        


tests = (
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 1, 2, 1], [1, 1, 1, 2]),
    ([1281, 1, 2], [1, 2, 1281]),
    (
        [995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756],
        [274, 303, 334, 488, 502, 546, 568, 709, 756, 995, 997, 999],
    ),
    (
        [648, 298, 568, 681, 795, 356, 603, 772, 373, 50, 253, 116],
        [50, 116, 253, 298, 356, 373, 568, 603, 648, 681, 772, 795],
    ),
)

for test, solution in tests:
    student_answer = [0] * len(test)
    counting_sort(test, student_answer)
    if student_answer != solution:
        print(
            "Feilet for testen {:}, resulterte i listen ".format(test)
            + "{:} i stedet for {:}.".format(student_answer, solution)
        )