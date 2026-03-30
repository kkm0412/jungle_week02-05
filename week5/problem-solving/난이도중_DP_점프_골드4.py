# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

#남은 돌의 개수, 이전에 이동한 돌을 기록해서 0까지 도달하는 것임 목표

N, M = map(int,input().split())
small = set()
for _ in range(M):
    small.add(int(input()))  
inf = 10001
jump = 2 * int(N**0.5)
#dp[i][j] => i는 돌. j는 점프크기 값은 점프 수
dp = [[inf] * jump for _ in range(N+1)]
dp[1][0] = 0
if 2 not in small:
    dp[2][1] = 1

for i in range(2, N+1):
    if i in small:
            continue
    for j in range(1, jump):
        if j-1 >0 and j <i and j-1 < jump:
            dp[i][j] = min(dp[i-j][j-1] +1, dp[i][j])
        if j < i and j < jump:
            dp[i][j] = min(dp[i-j][j] +1, dp[i][j])
        if j < i and j+1 < jump:
            dp[i][j] = min(dp[i-j][j+1] +1, dp[i][j])

result = min(dp[N])
if result >= inf:
    print(-1)
else:
    print(result)