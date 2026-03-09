# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

for c in range(C):
    inputs = list(input().split(' '))
    n = int(inputs[0])
    scores= list(inputs[1:])


    total_score = 0
    for score in scores:
        total_score += int(score)
    avg_score = total_score / n
    
    above_count = 0
    for score in scores:
        if avg_score < int(score):
            above_count += 1
    result = round(above_count/n * 100, 3)
    print(result, "%")