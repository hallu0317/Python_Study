import sys
import math

cnt = int(sys.stdin.readline())

for i in range(cnt):
    n, m = map(int, sys.stdin.readline().split())
    print(math.factorial(m) // (math.factorial(n) * math.factorial(m-n)))
