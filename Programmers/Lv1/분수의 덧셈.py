import math
def solution(denum1, num1, denum2, num2):
    n1 = denum1 * num2 + denum2 * num1
    n2 = num1 * num2
    answer = [n1//math.gcd(n1,n2),n2//math.gcd(n1,n2)]
    return answer