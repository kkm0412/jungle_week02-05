# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())

queue = deque(range(1,N+1))

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)
print(queue[0])