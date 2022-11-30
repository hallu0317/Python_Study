def solution(numbers):
    answer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(0, len(numbers)):
        answer.remove(numbers[i])

    return sum(answer)