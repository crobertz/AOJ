# ALDS1_1_D
# Maximum profit

N = int(input())

maxv = -float('inf')
minv = 0

for i in range(N):
    current = int(input())
    if i == 0:
        minv = current
    else:
        maxv = max(maxv, current -  minv)
        minv = min(minv, current)

print(maxv)
