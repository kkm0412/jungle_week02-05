# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

n = int(input())
def tile(n):

    if n == 1:
        return 1
    if n == 2:
        return 2
    x1 = 1
    x2 = 2
    for i in range(3, n+1):
        x = x1 + x2
        x1 = x2
        x2 = x % 15746
        
    return x2


print(tile(n)%15746)