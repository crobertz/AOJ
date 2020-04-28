N = int(input())
A = [int(n) for n in input().split()]

def bubbleSort(A, N):
    flag = 1 # adjacent element is out of order
    swaps = 0 # count number of swaps
    while flag:
        flag = 0
        for j in range(N-1):
            current = A[j]
            if current > A[j+1]:
                A[j] = A[j+1]
                A[j+1] = current
                flag = 1
                swaps += 1

    return swaps

swaps = bubbleSort(A, N)
print(' '.join([str(n) for n in A]))
print(swaps)
