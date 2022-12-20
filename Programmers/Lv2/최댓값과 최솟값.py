def solution(s):
    tmp = []
    answer = ""
    list = s.split(" ")

    for num in list:
        tmp.append(int(num))

    answer = str(min(tmp)) + ' ' + str(max(tmp))
    return answer