# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

N = int(input())

works = [{'time': 0, 'before':0, 'afters':[], 'after_time':[]} for _ in range(N+1)]
        #작업시간, 선행 갯수, 후행 관계, #선행작업 걸린 시간들
for i in range(1, N+1):
    x = list(map(int,input().split()))
    works[i]['time'] = x[0]
    works[i]['before'] = x[1]
    if x[1] != 0:
        for j in range(2, len(x)):
            works[x[j]]['afters'].append(i)

# print(works)

visited = [0]
finish = [0] * (N+1)    #완료 시간

while len(visited) != (N +1):
    afters_list = []    #다음 작업들
    for i in range(1, len(works)):  #처음주터 다시 검색
        if i not in visited and works[i]['before'] ==0: #안 했고, 선행작업 없는 것들
            visited.append(i)

            #이전 선행 작업들 시간 불러오기
            late_after = 0
            if len(works[i]['after_time']) !=0:
                late_after = max(works[i]['after_time'])

            #이전 선행작업중 가장 빨리 늦게끝난거 포함
            try_work = works[i]['time']+ late_after
            finish[i] = try_work
            #후행 작업들에게 알리기
            for after in works[i]['afters']:
                afters_list.append(after) 
                works[after]['after_time'].append(try_work)
    # total_time += try_work
    for after in afters_list:
        works[after]['before'] -= 1

total_time = max(finish)
print(total_time)