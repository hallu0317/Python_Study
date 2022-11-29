def solution(n):
    answer = []
    num = str(n)

    for i in range(0, len(num)):
        answer.append(int(num[i]))
    answer.reverse()

    return answer