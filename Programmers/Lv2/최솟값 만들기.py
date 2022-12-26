def solution(A, B):
    answer = 0
    listA = sorted(A)
    listB = sorted(B, reverse=True)

    for i in range(0, len(listA)):
        answer += listA[i] * listB[i]
        print(answer)
    return answer