def solution(array):
    answer = 0
    array2 = list(set(array))
    cnt = []
    for i in range(len(array2)):
        cnt.append(array.count(array2[i]))
    if cnt.count(max(cnt))>=2:
        return -1
    else:
        answer = array2[cnt.index(max(cnt))]
    return answer