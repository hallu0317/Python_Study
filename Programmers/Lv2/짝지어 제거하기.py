def solution(s):
    answer = 0
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        return 1

    return answer