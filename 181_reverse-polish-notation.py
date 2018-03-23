'''
You are given a long expression in postfix notation, which contains integer values and operations:

    add and sub for + and -;
    mul, div and mod for *, / and remainder;
    sqrt for taking square root.

You are to calculate the result.

Input data contains the expression, which may consist of few hundreds tokens.
Answer should contain single integer value - the result.

Example:

input data:
70 11 mul 5 div 219 add 28 26 6 sub 6 sub div mul 448 7 mul sqrt add

answer:
802
'''
operators = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x // y,
    'mod': lambda x, y: x % y,
    'sqrt': lambda x: x ** 0.5
}
stack = []

test = input().split()

for o in test:
    if o.isdigit():
        stack.append(int(o))
    else:
        if o == 'sqrt':
            x = stack.pop()
            stack.append(int(operators[o](x)))
        else:
            y, x = stack.pop(), stack.pop()
            stack.append(operators[o](x, y))

print(*stack)
