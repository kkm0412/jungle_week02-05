# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
# N = int(input())
# nums = list(map(int,input().split()))
# nums.sort()
# small = nums[len(nums)-1]
# A = 0
# B = 0
# def finder(target, left, right):
#     if left >= right:
#         return nums[left]    
#     mid = (left + right) //2
#     if nums[mid] < target:
#         return finder(target, mid, right)
#     elif nums[mid]> target:
#         return finder(target, left, mid - 1)
#     else:
#         return nums[mid]
# results = {}

# for i in range(N-1, -1, -1):
#     target = -nums[i]
#     b = finder(target, 0, N-1)
#     if small > i + b:
#         small = nums[i] + b
#         A = nums[i]
#         B = b


# if A < B:
#     print(A, B)
# else:
#     print(B, A)

#두 포인터 문제로 푸는것을 권장하여 두 포인터 방식으로 바꿔봄
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
i = 0
j = N -1
small = nums[j] + nums[i]
A = nums[i]
B = nums[j]
while j > i:
    x = nums[i] + nums[j]
    if abs(small) > abs(x):
        small = x
        A = nums[i]
        B = nums[j]
    if x == 0:
        break
    elif x > 0:
        j -= 1
    elif x < 0:
        i += 1
print(A, B)