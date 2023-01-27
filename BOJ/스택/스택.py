import sys
n = int(sys.stdin.readline())

stack = []
# stack = LIFO 
for i in range(n):
    # 공백을 기준으로 문자열를 잘라서 저장
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        stack.append(word[1])

    elif word[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif word[0] == 'size':
        print(len(stack))

    elif word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top은 스택에 가장 최근(나중)에 들어온 값을 의미
    elif word[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])