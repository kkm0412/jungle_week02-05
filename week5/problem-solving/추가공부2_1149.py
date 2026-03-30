# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

#dp[i][j]에서 i는 현재 집, j는 0, 1, 2가 각각 빨 초 파. 값은 총 색칠 비용
N = int(input())
house = [[0]* 3 for _ in range(N)]
for i in range(N):
    x = (list(map(int,input().split())))
    house[i][0] = x[0]
    house[i][1] = x[1]
    house[i][2] = x[2]

dp = [[0] * 3 for _ in range(N)]
dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + house[i][2]

print(min(dp[N-1]))