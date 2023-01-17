def solution(dartResult):
    answer = 0
    s = ''
    temp = []

    for dart in dartResult:
        if dart.isdigit():
            s += dart
        elif dart == 'S':
            temp.append(int(s) ** 1)
            s = ''
        elif dart == 'D':
            temp.append(int(s) ** 2)
            s = ''
        elif dart == 'T':
            temp.append(int(s) ** 3)
            s = ''
        elif dart == '*':
            if len(temp) > 1:
                temp[-1] = temp[-1] * 2
                temp[-2] = temp[-2] * 2
            else:
                temp[-1] = temp[-1] * 2
        elif dart == '#':
            temp[-1] = temp[-1] * -1
    answer = sum(temp)
    return answer