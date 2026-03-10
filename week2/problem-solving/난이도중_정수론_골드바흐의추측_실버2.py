# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

#소수 만들기는 난이도 하 정수론(problem/1978)으로 이전에 했으니 라이브러리를 찾아봄.
# from primePy import primes
# primes = primes.upto(10000)
# print(primes)

# for t in range(0,T):
#     ablePrimes =[]
#     num = int(input())
#     for prime in primes:
#         if prime >= num:
#             break
#         else:
#             if num-prime in primes:
#                 if prime <= num-prime:
#                     ablePrimes.append((num - 2*prime, prime, num - prime))
#     # print(ablePrimes)
#     # print(min(ablePrimes, key= lambda x: x[0])) # lambda 사용해보기
#     result = min(ablePrimes, key= lambda X: X[0])
#     print(result[1],"", result[2])

#백준에서 라이브러리 사용이 안되서 이전것을 긁어서 다시 짬
import math

limit = 10000
primes = list([1] * (limit+1))   #0~1000까지 0 포함해서 1001
primes[0], primes[1] = 0, 0 #0, 1 제외
for i in range(2,math.ceil(math.sqrt(limit)+1)):
    if primes[i] == 1:
        pointer = i * 2
        while pointer <= limit:
            primes[pointer] = 0
            pointer += i            
# print(primes)

T = int(input())

for t in range(0,T):
    ablePrimes =[]  #가능한 소수 튜플 (차이, 소수1, 소수2)
    num = int(input())
    for i in range(0, num//2 +1):
        if primes[i] == 1:
            if primes[i] >= num:
                break
            else:
                if primes[num-i]:
                    if i <= num-i:
                        ablePrimes.append((num - 2*i, i, num - i))
    # print(ablePrimes)
    # print(min(ablePrimes, key= lambda x: x[0])) # lambda 사용해보기
    result = min(ablePrimes, key= lambda X: X[0])
    print(result[1], result[2])