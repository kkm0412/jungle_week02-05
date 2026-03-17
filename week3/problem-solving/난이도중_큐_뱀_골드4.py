# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
from collections import deque

body = [(0,0)]
snake = deque(body)
direction = [(0,1),(1,0),(0,-1),(-1,0)]
dir = deque(direction)

#몸이 이동하는거
def snake_move():
    global iscollide
    # current_dir = dir[0]
    head = (snake[0][0]+ dir[0][0], snake[0][1]+ dir[0][1])
    if collision_check(head):
        iscollide = True
    snake.appendleft(head)
    if snake_eat(apple, head) != True:
        snake.pop()
    
#사과먹으면 길어지는거
def snake_eat(apple, head):
    if head in apple:
        apple.remove(head)
        return True
#벽 부딪히거나 몸하고 부딪힐때
def collision_check(head):
    if head in snake or head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
        if not snake_eat(apple, head):
            return True
    return False
def turn(turn_dir):
    if turn_dir == "L":
        dir.rotate(1)
    elif turn_dir == "D":
        dir.rotate(-1)

time = 0
apple = []
do = deque([])
N = int(input())
  
K = int(input())

for _ in range(K):
    r, h = map(int, input().split())
    apple.append((r-1,h-1))
L = int(input())
X = C = None
for _ in range(L):
    inputs = input().split()
    X = int(inputs[0])
    C = inputs[1]
    do.append([X,C])

iscollide = False
while iscollide == False:
    time += 1
    snake_move()
    if do and time == do[0][0]:
        turn(do[0][1])
        do.popleft()
print(time)