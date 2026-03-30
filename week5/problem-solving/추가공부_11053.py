# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#계산해야할 배열: 각 숫자에서 가장 긴 배열;

#dp[i] #현재 위치이고. 값은 그 위치에서 가장 큰 수열 크기

N = int(input())

array = list(map(int,input().split()))

dp = [1] * N
dp[0] = 1
for j in range(1, N):
    for i in range(j):
        if array[j] >array[i]:
            dp[j] = max(dp[i] + 1, dp[j])
print(max(dp))
