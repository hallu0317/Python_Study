def solution(s):
    answer = False
    cnt = 0
    s = s.lower()
    for i in range(0,len(s)):
        if(s[i]=='p'):
            cnt+=1
        elif(s[i]=='y'):
            cnt-=1
    if(cnt==0):
        answer = True
    return answer