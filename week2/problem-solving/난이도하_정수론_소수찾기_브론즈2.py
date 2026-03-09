# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978


# 먼저 소수 리스트 (1이면 소수, 0이면 소수 아님) 만들기

#소수 리스트 만들기
limit = 1000
prime = list([1] * (limit+1))   #0~1000까지 0 포함해서 1001
prime[0], prime[1] = 0, 0 #0, 1 제외
for i in range(2,limit+1):
    if prime[i] == 1:
        pointer = i * 2
        while pointer <= limit:
            prime[pointer] = 0
            pointer += i
# print(prime) #테스트용

N = int(input())
count = 0
nums = list(map(int, input().split(" ")))
# nums = list(nums)
for i in range(0,N):
    if prime[nums[i] ] == 1:
        # print(i, nums[i])
        count += 1

print(count)