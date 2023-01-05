n = int(input())
tmp = []
for i in range(n):
    tmp.append(input())

answer = list(tmp[0])
for i in range(n):
    for j in range(len(answer)):
        if answer[j] == tmp[i][j]:
            continue
        else:
            answer[j] = '?'


print(''.join(answer))