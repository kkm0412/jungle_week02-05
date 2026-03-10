# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016
min, max = map(int, input().split(" "))
import math
limit = max
primes = list([1,-1] for i in range(limit+1 - min))   #0~1000까지 0 포함해서 1001
for i in range(limit+1 - min):
    primes[i][1] = i +min

# print(primes)

# primes[0], primes[1] = 0, 0 #0, 1 제외

for i in range(min, math.ceil(math.sqrt(limit)+1)):

    if primes[i][0] == 1:
        x = primes[i][1]
        pointer =  x * x
        while pointer <= limit:
            primes[pointer - min][0] = 0
            pointer += x * x

# primes[1] = 1
count = 0
for i in range(max+1 - min):
    if primes[i][0] == 1:
        count += 1
print(count)

#ㄴ 메모리 초과 남