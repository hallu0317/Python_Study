def solution(n):
    answer = 0
    for i in range(4,n+1):
        tmp = []
        for j in range(1,i+1):
            if i%j==0:
                tmp.append(i)
        if len(tmp)>=3:
            answer += 1
    return answer