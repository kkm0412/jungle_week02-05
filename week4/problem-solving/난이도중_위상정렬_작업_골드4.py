# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

N = int(input())

works = [{'time': 0, 'before':0, 'afters':[]} for _ in range(N+1)]#작업시간, 선행 갯수, 후행 관계
for i in range(1, N+1):
    x = list(map(int,input().split()))
    works[i]['time'] = x[0]
    works[i]['before'] = x[1]
    if x[1] != 0:
        for j in range(2, len(x)):
            works[x[j]]['afters'].append(i)

# print(works)

visited = [0]

while len(visited) != (N +1):
    afters_list = []
    for i in range(1, len(works)):
        if i not in visited and works[i]['before'] ==0:
            visited.append(i)
            try_work = works[i]['time']
            for after in works[i]['afters']:
                # works[after]['before'] -= 1 
                # 여기서 처리하면 1번 일 하고 이후에 일해야 되는데 동시에 일하게 됨
                afters_list.append(after) 
                works[after]['time'] += try_work
    # total_time += try_work
    for after in afters_list:
        works[after]['before'] -= 1

total_time = 0
for i in range(1, N+1):
    if total_time < works[i]['time']:
        total_time = works[i]['time']
print(total_time)