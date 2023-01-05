N = int(input())
tmp = []
for i in range(N):
  a = int(input())
  tmp.append(a)

tmp.sort()
for i in range(N):
    print(tmp[i])