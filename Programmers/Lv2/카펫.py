def solution(brown, yellow):
    answer = []
    yx = 0
    yy = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yx = yellow // i
            yy = i
            if yx * 2 + yy * 2 + 4 == brown:
                answer.append(yx + 2)
                answer.append(yy + 2)

                return sorted(answer, reverse=True)
    return answer