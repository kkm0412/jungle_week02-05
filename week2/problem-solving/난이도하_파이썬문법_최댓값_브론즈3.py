# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []
for i in range(0,9):
    nums.append(int(input()))
# print(nums)
big = 0
count = 0
for i in range(0,9):
    if big < nums[i]:
        big = nums[i]
        count = i+1
print(big)
print(count)