# ALDS1_2_C
# Stable sort

import copy

def BubbleSort(C, N):
    for i in range(N):
        for j in [N - k for k in range(1, N-i)]:
            if C[j][-1] < C[j-1][-1]:
                C[j], C[j-1] = C[j-1], C[j]

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][-1] < C[minj][-1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]

N = int(input())
cards = input().split()

def suitorder(cards):
    order = {c[-1]:[] for c in cards}
    for c in cards:
        order[c[-1]].append(c[0])
    return order

cards_bubble = copy.copy(cards)
BubbleSort(cards_bubble, N)
cards_select = copy.copy(cards)
SelectionSort(cards_select, N)

stability_bubble = suitorder(cards_bubble) == suitorder(cards)
stability_select = suitorder(cards_select) == suitorder(cards)

def stable(stability):
    if stability:
        return 'Stable'
    else:
        return 'Not stable'

print(' '.join(cards_bubble))
print(stable(stability_bubble))
print(' '.join(cards_select))
print(stable(stability_select))