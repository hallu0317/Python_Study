import sys
x = int(sys.stdin.readline())


for i in range(x):
    f = int(sys.stdin.readline())
    ho = int(sys.stdin.readline())
    dp = [n for n in range(1, ho+1)]
    for j in range(0, f):
        for k in range(1, ho):
            dp[k] += dp[k-1]
    print(dp[-1])



