def solution(s):
    answer = sorted(s)
    answer.sort(reverse=True)
    return "".join(answer)