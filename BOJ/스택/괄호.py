import sys

n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline()
    stack = []
    for s in word:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack)==0:
        print('YES')
    else:
        print('NO')
