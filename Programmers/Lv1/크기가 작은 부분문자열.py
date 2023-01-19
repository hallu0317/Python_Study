def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
    return answer

# def solution(t, p):
#     answer = 0
#     temp = ""
#     res = []
#     idx = 0
#     while len(res) <= len(t) - len(p):
#         if len(temp) < len(p):
#             for i in range(idx, idx + len(p)):
#                 temp += t[i]
#         else:
#             res.append(int(temp))
#             temp = ""
#             idx += 1
#
#     for num in res:
#         if num <= int(p):
#             answer += 1
#     return answer