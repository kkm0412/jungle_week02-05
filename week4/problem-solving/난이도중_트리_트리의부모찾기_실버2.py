# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

from collections import deque
N = int(input())

graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
visited [1] = True

parents = [0] * (N+1)

#bfs
queue = deque([1])

while len(queue) != 0:
    x = queue.popleft()
    childs = graph[x]
    for child in childs:
        if not visited[child]:
            visited[child] = True
            parents[child] = x
            queue.append(child)

for i in range(1, N+1):
    print(parents[i])