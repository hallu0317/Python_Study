def solution(n):
    answer = 0
    tmp = str(n)

    for i in range(0, len(tmp)):
        answer += int(tmp[i])

    return answer