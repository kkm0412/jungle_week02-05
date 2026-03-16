# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

A, B, C = map(int,input().split())

x = 1
def square(b):
    if b == 1:
        return A%C
    half = square(b//2)
    if b % 2 == 0:
        return (half *half) % C
    else:
        return (half * half * A) %C 
print(square(B))