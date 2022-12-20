import math
bro1, bro2 = map(int,input().split(' '))
cnt = int(input())

for i in range(1,cnt+1):
	if i%2==0:
			bro1 = bro1 + math.ceil(bro2/2)
			bro2 = math.floor(bro2/2)
	else:
			bro2 = bro2 + math.ceil(bro1/2)
			bro1 = math.floor(bro1/2)

print(bro1, bro2)