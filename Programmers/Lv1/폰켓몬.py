def solution(nums):
    answer = 0
    tmp = list(set(nums))

    if len(nums) // 2 > len(tmp):
        answer = len(tmp)
    else:
        answer = len(nums) // 2
    return answer