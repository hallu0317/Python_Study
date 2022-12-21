t = int(input())

for i in range(t):
    result = ""
    num, word = input().split()
    for s in word:
        result += s * int(num)
    print(result)