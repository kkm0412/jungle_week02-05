# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# 종이를 반으로 분할


# 더 분할 할 수 있는지 확인.
#분할 가능하면 계속 분할.

#더 이상 분할 불가능할때부터

# 자신이 여러 색을 가지고 있으면 2 리턴
# 자신이 하나의 색을 가지고 있으면 0 또는 1을 리턴
# 2를 리턴하기 전에 0과 1의 갯수를 리턴

N = int(input())

papers = [[-1] * (N + 1) for i in range(N+1)]

for i in range(1, N+1):
    color = list(map(int, input().split(" ")))
    for j in range(1, len(color)+1):
        papers[i][j] = color[j-1]

# print(papers)

white = blue = 0

def divider(n, i, j):   #사각형 크기, 좌표 y, x
    global white
    global blue
    if n == 1:
        return papers[i][j]
    check = []
    check.append(divider(n//2, i, j)) #제 2사분면
    check.append(divider(n//2, i, n//2+j))    #제 1사분면
    check.append(divider(n//2, n//2 + i, j))    #제 3사분면
    check.append(divider(n//2, n//2 + i, n//2 + j))       #제 4사분면
    
    if len(set(check)) == 1 and check[0] != 2:
        # print(n,i,j, check)
        return check[0]
    else:
        # print(n,i,j, check)
        for x in check:
            if x == 0:
                white += 1
            elif x == 1:
                blue += 1
        return 2

result = divider(N, 1, 1)

if result == 2:
    print(white)
    print(blue)
elif result == 0:   #통채로 하얀색
    print(1)
    print(0)
else:   #통채로 파란색
    print(0)
    print(1)