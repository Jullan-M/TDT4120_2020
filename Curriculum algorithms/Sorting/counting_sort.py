# A: unsorted list; k: largest integer in A; B: sorted output; C: cumulative count
def counting_sort(A, k):
    n = len(A)
    B = [0 for i in range(n)]
    C = [0 for i in range(k+1)]
    # Count every integer from 0 to k
    for i in range(n):
        C[A[i]] += 1
    
    # Cumulative sum of integer counts from 0 to k
    for j in range(1, k+1):
        C[j] += C[j-1]
    
    # The sorting loop is backwards so that the algorithm is stable
    for k in range(n-1, -1, -1):
        C[A[k]] -= 1 # This comes before the sorting because python uses 0-indexed lists (as opposed 1-indexed as in the book)
        B[C[A[k]]] = A[k]
    return B

A = [3,5,2,6,1,7,9,8,4]
sorted_list = counting_sort(A,9)
print(sorted_list)