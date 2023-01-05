numA, numB, numC = map(int,input().split())
tmp = []
tmp.append(numA)
tmp.append(numB)
tmp.append(numC)

tmp.sort()
print(tmp[1])