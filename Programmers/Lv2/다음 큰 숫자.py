def solution(n):
    answer = 0
    b = format(n, 'b')
    tmp2 = b.count('1')

    temp = 0
    while True:
        n = n + 1
        b2 = format(n, 'b')
        if b2.count('1') == tmp2:
            temp = b2
            break

    answer = int(temp, 2)
    return answer