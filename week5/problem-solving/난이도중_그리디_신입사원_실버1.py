# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

T = int(input())

for _ in range(T):
    N = int(input())
    person = []
    count = 1
    for i in range(N):
        x, y = map(int,input().split())
        person.append((x,y))



    person.sort(key= lambda x: x[0])
    top = person[0][1]
    for i in range(1, len(person)):
        if top > person[i][1]:
            count += 1
            top = person[i][1]

    print(count)