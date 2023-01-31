import sys
n = sys.stdin.readline().split()
temp1 = []
answer = 0
for _ in range(int(n[0])):
    temp1.append(sys.stdin.readline())

for _ in range(int(n[1])):
    if sys.stdin.readline() in temp1:
        answer +=1

print(answer)