# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

pointer = -1
output = []

def push(x):
    global pointer
    pointer += 1
    stack[pointer] = x
    # print(pointer)

def pop():
    global pointer
    if pointer != -1:
        popped_num = stack[pointer]
        stack[pointer] = None
        pointer -= 1
        output.append(popped_num)
    else:
        output.append(-1)

def size():
    global pointer
    output.append(pointer + 1)

def empty():
    global pointer
    if pointer == -1:
        output.append(1)
    else:
        output.append(0)
    
def top():
    global pointer
    if pointer != -1:
        output.append(stack[pointer])
    else:
        output.append(-1)
    
#입력
N = int(input())
stack = [None] * N

for i in range(N):
    inputs = list(input().split())
    # print(inputs)
    if inputs[0] == 'push':
        push(int(inputs[1]))
    elif inputs[0] == "pop":
        pop()
    elif inputs[0] =="size":
        size()
    elif inputs[0] =="empty":
        empty()
    elif inputs[0] == "top":
        top()
    else:
        print("잘못 입력하였습니다")

print("\n".join(map(str, output)))
        

