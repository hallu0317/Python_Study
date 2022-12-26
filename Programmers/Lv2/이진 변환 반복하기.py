def solution(s):
    answer = []
    convert = 0
    cnt = 0

    while s!='1':
        cnt += s.count('0')
        s = s.replace('0','')
        s = format(len(s),"b")
        convert += 1
    answer = [convert, cnt]
    return answer