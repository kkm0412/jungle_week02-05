# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

#dfs를 다돌고 다른 노드로 이동.
#그 노드가 visited가 아닐때만 다시 dfs 돌기

N, M = map(int, input().split())

graph = {}
for n in range(1, N+1):
    graph[n] = []

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

link_list = 0   #연결 리스트 수

visited = {}
for i in range(1, N+1):
    visited[i] = False


def dfs(graph, current, start, stack):
    if visited[current]:
        return
    visited[current] = True
    v = graph[current]
    for x in v:
        if not visited[x]:
            stack.append(x)
    while len(stack)!= 0:
        dfs(graph, stack.pop(), start, stack)
    if current == start:
        global link_list
        link_list += 1 #dfs 이므로 시작지점이랑 현재 노드 지점이 같을 때 한번 추가하면 됨

for i in range(1, N+1):
    dfs(graph, i, i, [])    

print(link_list)