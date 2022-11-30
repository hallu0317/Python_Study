def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(absolutes)):
        if signs[i] == True:
            absolutes[i] = absolutes[i]
        else:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)