# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
from collections import deque
n, k = map(int,input().split())

coins = []
for _ in range(n):
    x = int(input())
    coins.append(x)

queue = deque([(0,0)])#사용횟수, 현재비용
visited = [False] * (k+1)
coins.sort()
coins.reverse()
is_find = False
# print(coins)
#값이 큰 동전부터 시도,
while len(queue) != 0 and not is_find:
    cur = queue.popleft()
    
    for coin in coins:
        if coin + cur[1] < k and not visited[coin + cur[1]]:
            visited[cur[1]+ coin] = True
            queue.append((cur[0]+1, cur[1]+ coin))
        elif coin + cur[1] == k:
            print(cur[0] + 1)
            is_find = True
            break
if not is_find:
    print(-1)