# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

#남은 돌의 개수, 이전에 이동한 돌을 기록해서 0까지 도달하는 것임 목표

N, M = map(int,input().split())
inf = 10001 #도달 못할시 무한 적용
small =  []
for _ in range(M):
    small.append(int(input()))  

#dp[i][j] => i는 점프수. j는 돌. 값은 점프크기
jump = int(2 * (N ** 0.5))
dp = [[0] * jump for _ in range(N + 1)]
dp[2][1] = 1

for j in range(jump+1):
    for i in range(2, N+1):
        if i in small:
            continue
        x = dp[i][j]
        if x != 0:
            if i+x-1 <= N:
                dp[i+x-1][j+1] = x-1
            if i+x <= N:
                dp[i+x][j+1] = x
            if i+x+1 <= N:
                dp[i+x+1][j+1] = x+1
print(min(dp[N]))

