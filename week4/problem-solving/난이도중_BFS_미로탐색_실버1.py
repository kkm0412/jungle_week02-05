# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
from collections import deque
N, M = map(int, input().split())
miro = [[] for _ in range(N)]
for i in range(N):
    miro[i] = list(map(int, list(input())))
cnt = 1
queue = deque([(0,0,cnt)])
visited = [(0,0)]

while len(queue) != 0:
    current = queue.popleft()
    x = current[0]
    y = current[1]
    dist = current[2]
    if x -1 >=0 and miro[x-1][y] == 1 and (x-1, y) not in visited:
        queue.append((x-1,y, dist+1))
        visited.append((x-1,y))
    if y -1 >=0 and miro[x][y-1] == 1 and (x, y-1) not in visited:
        queue.append((x,y-1, dist+1))
        visited.append((x,y-1))
    if x +1 <N and miro[x+1][y] == 1 and (x+1, y) not in visited:
        queue.append((x+1,y, dist+1))
        visited.append((x+1,y))
    if y +1 <M and miro[x][y+1] == 1 and (x, y+1) not in visited:
        queue.append((x,y+1, dist+1))
        visited.append((x,y+1))
    if x == N-1 and y == M-1:
        cnt = dist
        break
print(cnt)