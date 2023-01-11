def solution(sizes):
    answer = 0
    tmp1 = []
    tmp2 = []

    for i in range(len(sizes)):
        tmp1.append(max(sizes[i]))

    for i in range(len(sizes)):
        tmp2.append(min(sizes[i]))

    answer = max(tmp1) * max(tmp2)
    return answer