# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

N = int(input())
W = [[]*N for i in range(N)]
 
for i in range(N):
    W[i] = list(map(int, input().split()))
# print(W)

way = ()
for i in range(0,N):
    way = way + (i, )   #갈 수 있는 길
#print(way)
case = []
walked = []

def walk(start, current, walked, spend):
    if len(walked) == N:
        if W[current][start] != 0:  #base case
            spend += W[current][start]
            case.append(spend)

    else:
        for target in range(N):
            if target not in walked and W[current][target]!=0 :
                spend += W[current][target] #선행
                walked.append(target)
                walk(start, target, walked, spend) #재귀
                spend -= W[current][target] #취소
                walked.remove(target)
    #
walked.append(0)
walk(0,0,walked,0)
# print(case)
print(min(case))


# case = []   #지불 가능한 방법
# walked = [] #현재 밟아온 길
# def walk(start, before, current, walked, spend):
#     spend += W[before][current] 
#     if len(walked) == N:    #base case
#         spend += W[current][start]
#         case.append(spend)
#         print(walked)
#     else:
#         un_go = list(set(way) - set(walked))    #아직 안 간곳
#         for next in un_go:
#             if W[current][next] != 0:
#                 walked.append(next)
#                 walk(start, current, next, walked, spend)
#                 walked.remove(next)
#     spend -= W[before][current]
# for i in range(0, N):
#     walked.append(i)
#     walk(i,i,i,walked,0)
#     walked.remove(i)
# # print(case)
# print(min(case))