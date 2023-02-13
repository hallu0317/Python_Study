import sys

n = int(sys.stdin.readline())
v1 = 3
v2 = 5
res = 0
while n >= 0:
    if n % v2 == 0:
        res += n // v2
        print(res)
        break
    n -= v1
    res += 1
else:
    print(-1)
