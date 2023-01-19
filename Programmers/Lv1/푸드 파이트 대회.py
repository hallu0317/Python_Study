def solution(food):
    answer = ''
    s = []
    for i in range(1, len(food)):
        s.append(str(i))

    for j in range(len(s)):
        answer += s[j] * (food[j + 1] // 2)

    rev = answer[::-1]
    answer += '0' + rev

    return answer