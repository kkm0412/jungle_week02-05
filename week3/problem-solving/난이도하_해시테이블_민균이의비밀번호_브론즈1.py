# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

# 
N = int(input())
passwords = []
for i in range(N):
    pwd = input()
    rev_pwd = pwd[::-1]
    list_pwd = list(pwd)
    length = len(list_pwd)
    mid = list_pwd[length//2]

    passwords.append({"pwd": pwd, "rev_pwd":rev_pwd, "length":length, "mid":mid})

for i in range(N):
    isFound = False
    for j in range(N):
        if passwords[i]["pwd"] == passwords[j]["rev_pwd"]:
            print(passwords[i]["length"], passwords[j]["mid"])
            isFound = True
            break
    if isFound == True:
        break
