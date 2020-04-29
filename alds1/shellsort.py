# ALDS1_2_D
# Shell sort

import sys
import math

def insertionSort(A, n, g):
    count = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            count += 1
        A[j+g] = v
    
    return count

def shellSort(A, n, G):
    count = 0
    for g in G:
        count += insertionSort(A, n, g)
    return count

def main():
    # inputs
    n = int(input())
    A = [int(l) for l in sys.stdin.readlines()]

    G = []
    g = 0
    for i in range(100):
        g = 3*g + 1
        if g > len(A):
            break
        G.append(g)
    m = len(G)

    count = shellSort(A, n, G[::-1])

    # print output
    print(m)
    print(' '.join(list(map(str, G[::-1]))))
    print(count)
    for num in A:
        print(num)

if __name__ == "__main__":
    main()