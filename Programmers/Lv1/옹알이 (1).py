def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for inputs in babbling:
        for word in words:
            inputs = inputs.replace(word, '?')
        if inputs.replace('?', '') == '':
            answer += 1
    return answer