import sys

n = int(sys.stdin.readline())

cnt = 0
d = [0]*41
d[0] = 0
d[1] = 1

for i in range(2,n+1):
    d[i] = d[i-2] + d[i-1]
    cnt += 1

print(d[n], cnt-1)