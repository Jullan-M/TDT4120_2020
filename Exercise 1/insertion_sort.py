#!/usr/bin/python3
# coding=utf-8


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]

        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            A[j] = key
            j -= 1
            
    return A


if __name__ == "__main__":
    tests = [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([9, 7, 3, 5, 2, 6], [2, 3, 5, 6, 7, 9]),
        ([-1, 1, -1, 2], [-1, -1, 1, 2]),
    ]

    for test, solution in tests:
        answer = insertion_sort(test)
        if answer != solution:
            print(
                "`insertion_sort` feilet for listen {:}. ".format(test)
                + "Svaret skulle vært {:}, men var {:}.".format(
                    solution, answer
                )
            )
        else:
            print("Svaret var riktig!")
