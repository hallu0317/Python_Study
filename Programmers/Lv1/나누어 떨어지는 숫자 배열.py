def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer