def solution(s):
    tmp = []
    answer = ""
    list = s.split(" ")

    for i in list:
        tmp.append(int(i))

    answer = str(min(tmp)) + ' ' + str(max(tmp))
    return answer