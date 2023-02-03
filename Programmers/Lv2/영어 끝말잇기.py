def solution(n, words):
    answer = []
    temp = []

    for i in range(0, len(words)):
        if len(temp) == 0:
            temp.append(words[i])
        else:
            if words[i] not in temp and words[i][0] == words[i - 1][-1]:
                temp.append(words[i])
            else:
                temp.append(words[i])
                return [((i % n) + 1), ((i // n) + 1)]
                break

    return [0, 0]