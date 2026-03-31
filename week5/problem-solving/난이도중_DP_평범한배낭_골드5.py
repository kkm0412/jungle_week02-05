# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

n, k = map(int,input().split())

items = []
for _ in range(n):
    w, v = map(int,input().split())
    items.append((w,v))

dp = [[0] *(k+1) for _ in range(n+1)]

for w in range(1, k+1):
    for i in range(1, n+1):
        weight, value = items[i-1]
        if weight <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+ value)

print(max(max(dp)))