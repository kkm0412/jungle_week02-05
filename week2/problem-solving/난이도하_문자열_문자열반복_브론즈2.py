# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
#
T = int(input())

for i in range(0, T):
    rs = input().split()
    R = int(rs[0])
    S = list(rs[1])

    for alpha in S:
        print(alpha * R, end= "")
    print("")

