def solution(num, total):
    answer = []
    if total%num == 0:
        answer.append(total//num)
        i=1
        while(len(answer)!=num):
            answer.insert(0,total//num-i)
            answer.append(total//num+i)
            i+=1
    else:
        answer.append(total//num)
        answer.append(total//num+1)
        i=1
        while(len(answer)!=num):
            answer.insert(0,total//num-i)
            answer.append(total//num+1+i)
            i+=1
    return answer