#!/usr/bin/python3
# coding=utf-8


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        # Places A[i] into the sorted sublist [0....j-1]
        j = i - 1
        while j >= 0 and A[j] > key:
            # Moves each element one step to the right, as long as key<A[j]
            A[j + 1] = A[j]
            j -= 1
        # Place key to the correct position
        A[j+1] = key
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
