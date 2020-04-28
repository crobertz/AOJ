# ALDS_1_1B
# GCD

x, y = sorted([int(n) for n in input().split()])

# x < y

def gcd(y, x):
    if y % x == 0:
        return x
    else:
        return gcd(x, y % x)

print(gcd(y,x))
