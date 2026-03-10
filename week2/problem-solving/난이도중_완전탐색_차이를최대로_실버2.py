# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
N = int(input())

inputs = list(map(int,input().split(" ")))

nums = []
for i in range(0, N):
    nums.append((i, inputs[i]))

# N까지의 나열
# 전부 차이값 계산해서 덧셈
#그중 가장 큰거 찾기

# 찾아보니 itertools라이브러리의 permutations를 쓰면 빠르게 계산 가능하다고 함

intervals = []

def total_interval(nums: list):  #거리 계산
    interval_value = 0
    for i in range(0, N-1):
        interval_value += abs(nums[i][1] - nums[i+1][1])
    intervals.append(interval_value)

def total_arranger(nums: list, memory:list):
    #base case
    if len(memory) == N:
        total_interval(memory)
        return
    
    for num in nums:
        if num not in memory:
            memory.append(num)
            total_arranger(nums, memory)
            # memory.remove(num)    #같은 값이 들어가면 오류가 남.
            memory.pop()

total_arranger(nums, [])
print(max(intervals))



#초기 버전
# 동일한 값이 입력 될경우 memory에서 구분을 못하는 문제가 생김

# nums = list(map(int,input().split(" ")))
# intervals = []

# def total_interval(nums: list):  #거리 계산
#     interval_value = 0
#     for i in range(0, N-1):
#         interval_value += abs(nums[i] - nums[i+1])
#     intervals.append(interval_value)

# def total_arranger(nums: list, memory:list):
#     #base case
#     if len(memory) == N:
#         total_interval(memory)
#         return
    
#     for num in nums:
#         if num not in memory:
#             memory.append(num)
#             total_arranger(nums, memory)
#             # memory.remove(num)    #같은 값이 들어가면 오류가 남.
#             memory.pop()