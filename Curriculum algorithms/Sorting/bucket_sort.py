from insertion_sort import insertion_sort

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[int(n*A[i])].append(A[i])

    for j in range(n):
        insertion_sort(B[j])

    res = []
    for i in range(0, len(B)):
        res += B[i]
    return res
