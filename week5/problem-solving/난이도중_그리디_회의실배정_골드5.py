# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
N = int(input())

I = []  #회의 입력
for n in range(N):
    i = list(map(int,input().split()))
    I.append((i[0], i[1]))

#회의가 최대한 빨리 끝나는것부터
I.sort(key = lambda x : x[0])
I.sort(key = lambda x : x[1])
# 끝나는 시간 순 다음으로는 시작하는 시간 순으로 나열
time = 0
count = 0
for i in I:
    if time <= i[0]:
        time = i[1]
        count+= 1
print(count)