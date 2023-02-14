import sys
n = int(sys.stdin.readline())

# if n % 2 == 1:
#     print('SK')
# else:
#     print('CY')

dp = [-1]*1001
dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'

for i in range(4,n+1):
    if dp[i-1] == 'SK' or dp[i-3] == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

print(dp[n])