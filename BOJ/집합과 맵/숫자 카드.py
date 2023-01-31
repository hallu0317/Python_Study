import sys

n = int(input())
temp = set(map(int, input().split()))

n2 = int(input())
temp2 = list(map(int, input().split()))

for i in temp2:
    if i in temp:
        print(1, end=' ')
    else:
        print(0, end=' ')