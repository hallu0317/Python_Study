N = int(input())
M = N
cycle = 0

while (True):
    tmp = M // 10 + M % 10
    M = M % 10 * 10 + tmp % 10
    tmp = M
    cycle += 1

    if(M==N):
        break

print(cycle)
