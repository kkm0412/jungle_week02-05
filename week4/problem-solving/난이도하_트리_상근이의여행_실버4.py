# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372


#그래프 문제임
#이게 왜 트리 문제야;;;;
#
from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    planes = {}
    for n in range(N+1):
        planes[n] = []
    for m in range(M):
        a, b = map(int, input().split())
        planes[a].append(b)
        planes[b].append(a)
    queue = deque([1])
    visited = []
    count = 0
    while len(queue) != 0:
        x = queue.popleft()

        can_go = planes[x]
        for y in can_go:
            if y not in visited:
                count += 1
                queue.append(y)
                visited.append(y)
    print(count)
    # print(N-1)
#처리과정
#아무곳에서 시작하면
#bfs 방식으로 전부 읽어와서 몇번인지 세기


