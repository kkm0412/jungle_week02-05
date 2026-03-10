# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

N = int(input())
# print(N)
board = [[0] * N for i in range(N)]
# print(board)
cnt = 0

def draw(x, y):
    for i in range(N):
        board[x][i] += 1
        board[i][y] += 1
        if x - i >= 0 and y - i >= 0:
            board[x-i][y-i] += 1
        if x - i >= 0 and y + i < N:
            board[x-i][y+i] += 1
        if x + i < N and y - i >= 0:
            board[x+i][y-i] += 1
        if x + i < N and y + i < N:
            board[x+i][y+i] += 1

def undraw(x, y):
    for i in range(N):
        board[x][i] -= 1
        board[i][y] -= 1
        if x - i >= 0 and y - i >= 0:
            board[x-i][y-i] -= 1
        if x - i >= 0 and y + i < N:
            board[x-i][y+i] -= 1
        if x + i < N and y - i >= 0:
            board[x+i][y-i] -= 1
        if x + i < N and y + i < N:
            board[x+i][y+i] -= 1

def queen(row):
    if row == N:
        global cnt
        cnt += 1
        return
    for i in range(N):
        if board[i][row] == 0:
            draw(i,row)
            queen(row+1)
            undraw(i, row)

queen(0)
print(cnt)

    
# print(len(ct))