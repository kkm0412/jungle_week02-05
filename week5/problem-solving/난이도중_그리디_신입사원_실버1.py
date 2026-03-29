# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

T = int(input())

for _ in range(T):
    N = int(input())
    person = []
    count = 0
    for i in range(N):
        x, y = map(int,input().split())
        person.append((x,y))

    #a가 가장 낮은 사람들중에서
    #a가 다음으로 낮은 사람들중 제일 b가 낮은 사람 기준으로 컷하기

    person.sort(key= lambda i : i[1],reverse=True)
    person.sort(key= lambda i : i[0],reverse=True)

    a = person[0][0]
    #a가 그다음으로 낮은사람 찾기
    y_cut = 100001
    for x in person:
        if x[0] != a:
            y_cut = x[1]
            break
    for x in person:
        if x[1] <= y_cut:
            break
        count +=1

    #b
    person.sort(key= lambda i : i[0],reverse=True)
    person.sort(key= lambda i : i[1],reverse=True)

    b = person[0][1]
    #a가 그다음으로 낮은사람 찾기
    x_cut = 100001
    for y in person:
        if y[1] != b:
            x_cut = y[0]
            break
    for y in person:
        if y[0] <= x_cut:
            break
        count +=1
        
    print(N - count)