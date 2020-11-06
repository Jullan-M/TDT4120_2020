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