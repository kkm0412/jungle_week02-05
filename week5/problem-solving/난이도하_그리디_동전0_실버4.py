# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

# 큰수로 역 나열하고
# 결과 출력하면됨
#
import sys
input = sys.stdin.readline


count = 0

n, k = map(int,input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input())

coins.sort(reverse=True)

for coin in coins:
    while coin <= k:
        k -=coin
        count+=1

print(count)