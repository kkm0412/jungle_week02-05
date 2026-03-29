# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

#남은 돌의 개수, 이전에 이동한 돌을 기록해서 0까지 도달하는 것임 목표

N, M = map(int,input().split())
inf = 10001 #도달 못할시 무한 적용
small =  []
for _ in range(M):
    small.append(int(input()))  

dp = [[inf] * (int((2*N)** 0.5) + 2) for _ in range(N + 1)]

\


#dp 안에는 최소 점프횟수와 직전 점프 수가 들어있음











    # small.add(N - int(input()))  #남은 돌의 수 기준이므로

# memo = {}

# def jump(n, prev):
#     if n <0 or prev < 1 or n in small:  #예외처리: 도착점 넘었거나 1칸 미만 움직이거나 작은돌 밟을 때
#         return -1
#     elif n == 0:
#         return 0
#     if (n,prev) in memo:   #메모이제이션  n있으면 계산 안하고 스킵
#         return memo[(n,prev)]
#     result_memory = [] #결과들 중 -1 안나오는것들 넣는용

#     result1 = jump(n-prev+1, prev-1)
#     if result1 != -1:
#         result_memory.append(result1)
#     result2 = jump(n-prev, prev)
#     if result2 != -1:
#         result_memory.append(result2)
#     result3 = jump(n-prev-1, prev+1)
#     if result3 != -1:
#         result_memory.append(result3)

#     if len(result_memory) == 0: #전부 -1이면
#         memo[(n,prev)] = -1
#         return -1
#     else:
#         result = 1+ min(result_memory)
#         memo[(n,prev)] = result #메모에 있는 값 비교하고 더 적으면 집어넣기
#         return result
    
# if N ==2:
#     print(1)
# else:
#     print(jump(N-2,1) + 1)