# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

n = int(input())

pc = {}
for i in range(1, n+1):
    pc[i] = []

m = int(input())

for _ in range(m):
    a, b = map(int,input().split())
    pc[a].append(b)
    pc[b].append(a)

print(pc)