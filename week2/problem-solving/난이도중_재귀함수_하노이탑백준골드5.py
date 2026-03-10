# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
# 3개     4개
# 1 3  a  1 2
# 1 2     1 3
# 3 2  b  2 3  a
#         1 2
#         3 1
#         3 2
#         1 2  b

# 1 3     1 3

# 2 1 a   2 3
# 2 3     2 1
# 1 3 b   3 1  a
#         2 3
#         1 2
#         1 3
#         2 3  b

# 1 3
# 1 2
# 3 2

# 홀수번 째 a b에서 위에는 a c 아래는 c b

def hanoi(n, start, via, end):
    if n == 3:
        #  print(start, via, end)
         print(start, end)
         print(start, via)
         print(end, via)
         print(start, end)
         print(via, start)
         print(via, end)
         print(start, end)
    else:
         hanoi(n-1, start, end, via)
         print(start,end)
         hanoi(n-1, via, start, end)

# hanoi(4, '1', '2', '3')
N = int(input())

print(2**N-1)
if (N<=20):
    hanoi(N,'1','2','3')