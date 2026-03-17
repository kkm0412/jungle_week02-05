# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
N = int(input())

K= []
for i in range(N):
    x = int(input())
    K.append(x)

K.sort()
# big이 k번째 값.
#이분탐색으로 값을 찾기.
#탐색 기준은 남은 수보다 작은 값
adds = []
adds = set(adds)
for i in range(N):
    for j in range(N):
        adds.add(K[i] + K[j])
# print(adds)

length = len(adds)
is_find = False

for i in range(len(K) - 1, -1, -1):
    if not is_find:
        for add in adds:
            if not is_find:
                if (K[i] - add) in K:
                    is_find = True
                    print(K[i])