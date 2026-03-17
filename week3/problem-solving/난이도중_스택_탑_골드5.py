# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

N = int(input())
tops = list(map(int,input().split()))

stack = []

memory = [] #(위치, 높이)
result = []
#기본적으로 탑을 놓을때
#현재 가장 높은 것만 memory에 저장해서 스택으로 쌓아놓기.
for top in tops:
    stack.append(top)
    collide = 0
    x = None
    
    while len(memory) != 0:
        x = memory.pop()
        if x[1] > top:
            collide = x[0]
            memory.append(x)
            break
    memory.append((len(stack),top))
    result.append(collide)

for top in result:
    print(top, end=" ")
