def solution(a, b):
    answer = ''
    temp = 0
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a - 1):
        temp += month[i]
    temp += b
    temp = temp % 7
    answer = day[temp]
    return answer