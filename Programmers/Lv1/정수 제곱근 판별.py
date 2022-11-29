import math
def solution(n):
    answer = -1
    if(n / int(math.sqrt(n)) == int(math.sqrt(n))):
        answer = (int(math.sqrt(n))+1)**2
    return answer