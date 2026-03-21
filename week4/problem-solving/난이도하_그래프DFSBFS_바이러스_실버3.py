# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
from collections import deque

n = int(input())

pc = {}
for i in range(1, n+1):
    pc[i] = []

m = int(input())

for _ in range(m):  #그래프 연결
    a, b = map(int,input().split())
    pc[a].append(b)
    pc[b].append(a)

queue = deque([1])  

infected = [1]  #감염된 PC

while len(queue) != 0:  #bfs
    x = queue.popleft()
    connected = pc[x]
    for com in connected:
        if com not in infected:
            infected.append(com)
            queue.append(com)

print(len(infected) - 1) # 1번 제외 감염된 pc수