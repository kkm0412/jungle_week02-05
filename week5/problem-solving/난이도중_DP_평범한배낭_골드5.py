# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 
# 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 특정 무게만큼 최대한 가치 높게 들고 갈 수 있도록 하기
# 특정 무게를 배열의 인덱스로 하여 

#bag[무게]{가치:[들어있는 물건]}

n, k = map(int,input().split())

items = []
for _ in range(n):
    w, v = map(int,input().split())
    items.append((w,v))

# #적은 무게순으로 오름차순 정렬
# items.sort(key=lambda x: x[0])

# bag = [{0:[0op]}]

# for weight in range(1, k):
#     for i in range(0, len(items)):
#         if items[i][0] <= weight:
            
#     #무게별로 넣을 수 있는 아이템 확인

#무게가 클때부터 시작
# dp는 가방이 아니라 점수판
# dp = [0] * (k+1)
# for w in range(k, 0 , -1):
#     for item in items:
#         if item[0] <= w:
#             dp[w] = max(dp[w-item[0]] + item[1], dp[w])
# print(max(dp))
dp = [0] * (k+1)
for item in items:
    for w in range(k, 0, -1):
        if item[0] <= w:
            dp[w] = max(dp[w-item[0]] + item[1], dp[w])
print(dp[k])
