count = int(input())
answer = 0

nums = list(map(int,input().split()))
nums.sort()

for i in range(count):
    answer += sum(nums)
    nums.pop()

print(answer)