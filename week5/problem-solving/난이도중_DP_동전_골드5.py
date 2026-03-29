# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

#
# dp[금액] = 방법수
T = int(input())

for t in range(T):
    N = int(input())
    coins = []
    inputs = list(map(int,input().split()))
    for x in inputs:
        coins.append(x)
    coins.sort()
    M = int(input())
    money = [0] * (M+1)
    money[0] = 1
    for coin in coins:
        for i in range(1, len(money)):
            if i-coin >=0:
                money[i] += money[i-coin]
    print(money[M])
#0원을 1가지 방법으로 두고.(결국 안 넣어도 방법이 하나이므로)
#1부터 M까지 차례대로 올라감.
#바텀 업 식으로
#특정 값에서 -동전을 하고 그 뺀 값에 방법이 있으면
#그 방법 + 1을 함 겹칠시 max. 겹칠시 그만큼 더함

