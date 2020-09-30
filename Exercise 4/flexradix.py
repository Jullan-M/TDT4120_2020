#!/usr/bin/python3
# coding=utf-8

def str2int(Aj, i):
    if len(Aj) >= i + 1:
        return ord(Aj[i]) - 96
    return 0

def counting_sort(A, B, i):
    n = len(A)
    C = 27*[0]

    for j in range(n):
        C[str2int(A[j], i)] += 1

    for j in range(1, 27):
            C[j] += C[j - 1]

    for k in range(n-1, -1, -1):
        C[str2int(A[k], i)] -= 1
        B[C[str2int(A[k], i)]] = A[k]


def flexradix(A, d):
    n = len(A)
    B = [A[i] for i in range(n)]
    
    # Counting-sort method
    for i in range(d-1, -1, -1):
        counting_sort(A, B, i)

    return B
                

tests = (
    (([], 1), []),
    ((["a"], 1), ["a"]),
    ((["a", "b"], 1), ["a", "b"]),
    ((["b", "a"], 1), ["a", "b"]),
    ((["ba", "ab"], 2), ["ab", "ba"]),
    ((["b", "ab"], 2), ["ab", "b"]),
    ((["ab", "a"], 2), ["a", "ab"]),
    ((["abc", "b"], 3), ["abc", "b"]),
    ((["abc", "b"], 4), ["abc", "b"]),
    ((["abc", "b", "bbbb"], 4), ["abc", "b", "bbbb"]),
    ((["abcd", "abcd", "bbbb"], 4), ["abcd", "abcd", "bbbb"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
)

for test, solution in tests:
    student_answer = flexradix(test[0], test[1])
    if student_answer != solution:
        print(
            "Feilet for testen {:}, resulterte i listen ".format(test)
            + "{:} i stedet for {:}.".format(student_answer, solution)
        )