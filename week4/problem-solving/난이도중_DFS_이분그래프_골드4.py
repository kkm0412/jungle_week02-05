# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

#bfs로
#레드(-1) 블루(1) 집어넣어서 정점 칠하기

from collections import deque

K = int(input())
for _ in range(K):
    V, E = map(int,input().split())
    is_divide = True
    graph = {}
    color = {}
    visited = {}
    for key in range(1, V+1):
        graph[key] = []
        color[key] = 0
        visited[key] = False
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])
    color[1] = -1
    visited[1] = True

    for t in range(1, V+1):
        if not visited[t]:
            queue = deque([t])
            color[t] = -1
            visited[t] = True
        while len(queue) != 0:
            x = queue.popleft()
            c = color[x]
            for num in graph[x]:
                if color[num] == 0:
                    color[num] = -c
                    visited[num] = True

                    queue.append(num)

                else:
                    if color[num] == c:
                        is_divide = False

            if not is_divide:
                break
    if is_divide:
        print("YES")
    else:
        print("NO")