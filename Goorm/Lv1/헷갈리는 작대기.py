user_input = input()
cnt1=0
cnti=0
cntl=0
cnt=0

for i in range(0,len(user_input)):
	if user_input[i] == '1':
		cnt1+=1
	elif user_input[i] == 'I':
		cnti+=1
	elif user_input[i] == 'l':
		cntl+=1
	elif user_input[i] == '|':
		cnt+= 1

print(cnt1)
print(cnti)
print(cntl)
print(cnt)