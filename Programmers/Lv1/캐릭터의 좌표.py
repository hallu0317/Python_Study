def solution(keyinput, board):
    answer = [0, 0]
    board = [board[0] // 2, board[1] // 2]
    for key in keyinput:
        if key == 'left' and answer[0] - 1 >= -board[0]:
            answer[0] -= 1
        elif key == 'right' and answer[0] + 1 <= board[0]:
            answer[0] += 1
        elif key == 'down' and answer[1] - 1 >= -board[1]:
            answer[1] -= 1
        elif key == 'up' and answer[1] + 1 <= board[1]:
            answer[1] += 1

    return answer