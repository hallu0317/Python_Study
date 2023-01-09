def solution(price, money, count):
    answer = 0
    p = 0
    for i in range(1, count + 1):
        p += price * i

    answer = p - money
    return 0 if money >= p else answer