# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

N = int(input())
rows = set()
cnt = 0
diag1 = set()   #좌위 대각선   
diag2 = set()   #좌하 대각선
def dfs(col):
    #base case
    if col == N:
        global cnt
        cnt += 1   
        return 
    
    for row in range(N):
        isOk = True

        if row in rows:
            isOk = False
        if (col - row) in diag1:
            isOk = False
        if (col + row) in diag2:
            isOk = False    
            
        if isOk:
            rows.add(row)
            diag1.add(col-row)
            diag2.add(col+row)
            dfs(col+1)
            rows.remove(row)
            diag1.remove(col-row)
            diag2.remove(col+row)
dfs(0)
print(cnt)

    
# print(len(ct))