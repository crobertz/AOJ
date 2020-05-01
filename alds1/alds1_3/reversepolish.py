# ALDS1_3_A
# Reverse polish notation

in_list = input().split()[::-1]

def add(x,y):
    return x + y

def mult(x,y):
    return x * y

def sub(x,y):
    return x - y

num_stack = []
op_dict = {'+':add, '-':sub, '*':mult}

while in_list:
    symbol_current = in_list.pop()
    if symbol_current in op_dict:
        op = op_dict[symbol_current]
        symbol_prev = num_stack.pop()
        symbol_prevprev = num_stack.pop()
        num_stack.append(op(symbol_prevprev, symbol_prev))
    else:
        num_stack.append(int(symbol_current))


print(num_stack.pop())