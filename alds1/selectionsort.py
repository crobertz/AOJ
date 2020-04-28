N = int(input())
A = [int(n) for n in input().split()]

def selectionSort(A, N):
    # counter for number of swaps
    swaps = 0

    for i in range(N):
        # select minimum element in A[i:]
        minj = i

        for j in range(i,N):
            if A[j] < A[minj]:
                minj = j

        # swap A[i] and A[minj]
        A[i], A[minj] = A[minj], A[i]
        # increment swap count
        if i < minj:
            swaps += 1

    return swaps

swaps = selectionSort(A, N)
print(' '.join(list(map(str, A))))
print(swaps)
