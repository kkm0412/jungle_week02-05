# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
# -가 나오면 괋로로 묶는다.

result = 0
blocks = list(input().split('-'))
for i in range(0, len(blocks)):
    if i == 0:
        nums = map(int, blocks[i].split('+'))
        for num in nums:
            result += num
    else:
        nums = map(int, blocks[i].split('+'))
        for num in nums:
            result -= num

print(result)