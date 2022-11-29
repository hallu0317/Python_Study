def solution(x):
    num = str(x)
    result = 0
    for i in range(0,len(num)):
        result += int(num[i])
    if(x%result == 0):
        return True
    return False