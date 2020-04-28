# ALDS1_1_C
# Prime numbers

import math

n = int(input())

count = 0


def isprime(x):
    for d in range(2,int(math.sqrt(x) + 1)):
        if x % d == 0:
            return False
    return True

for i in range(n):
    x = int(input())
    if isprime(x):
        count += 1

print(count)
