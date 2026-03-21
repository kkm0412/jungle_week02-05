# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
N = int(input())

gamemap = [[] * N for _ in range(N)]

stack = [(0,0)]

for i in range(N):
    p = list(map(int,input().split()))
    gamemap[i] = p

is_able = False
def dfs(cur):
    if gamemap[cur[0]][cur[1]] == 0:    #0일시 그자리에서 계속 재귀함
        return
    if gamemap[cur[0]][cur[1]] == -1:
        global is_able
        is_able = True
    else:
        x = gamemap[cur[0]][cur[1]]
        if cur[0] +x < N:
            dfs((cur[0]+x, cur[1]))
        if cur[1] +x < N:
            dfs((cur[0], cur[1]+x))

dfs(stack.pop())
if (is_able):
    print("HaruHaru")
else:
    print("Hing")