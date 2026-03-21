# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque
N, M, V = map(int,input().split())

graph = {}
for n in range(1,N+1):
    graph[n] = []

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort() #정점 여러개면 작은거 들어가야되서 인접리스트들 정렬필요 by ai
# stack = []
queue = deque([V])

dfs_result = []
bfs_result = []

def dfs(graph, current, visited, stack):
    if current in visited:
        return
    visited.append(current)

    dfs_result.append(current)
    nodes = graph[current]
    for node in reversed(nodes):    #작은것부터 들어가야되서 역순으로 스택에 집어넣음 by ai
        stack.append(node)
    while len(stack) != 0:
        dfs(graph, stack.pop(), visited, stack)

#bfs
def bfs(graph, queue, visited):
    while len(queue) != 0:
        current = queue.popleft()
        if current in visited:
            continue
        bfs_result.append(current)
        visited.append(current)
        nodes = graph[current]
        for node in nodes:
            queue.append(node)


dfs(graph, V, [], [])
bfs(graph, queue, [])
for i in dfs_result:
    print(i,end=" ")
print("")
for i in bfs_result:
    print(i,end=" ")
