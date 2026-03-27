# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
a = list(input())
b = list(input())

# 가로세로 a b의 문자들로 이루어진 표
x = [[0] * len(b) for _ in range(len(a))]


## 연속으로 문자열이 나올때
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             if i >0 and j>0:
#                 x[i][j] = x[i-1][j-1] +1

#순서대로 같은 문자(문자열 x)나올 때
for i in range(len(a)): 
    for j in range(len(b)):
        if a[i] == b[j]:
            if i >0 and j>0:
                x[i][j] = x[i-1][j-1] +1
            else:
                x[i][j] = 1
        else:
            if j >0:
                x[i][j] = x[i][j-1]
            if i >0:
                x[i][j] = max(x[i][j], x[i-1][j])
print(max(max(x)))