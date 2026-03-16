# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

# 아니 온갖 난리를 다 쳐도 시간초과 나오네 이걸 어찌 하라는거야
import sys
input = sys.stdin.readline
output = [] #ㄴ시간초과 방지용

class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data, next_data): #역 초기화
        if self.head == None:
            self.head = Node(data)
            station_id[data] = self.head
        if next_data != None:
            node = station_id[data]
            next_node = Node(next_data)
            node.next = next_node
            next_node.prev = node
            station_id[next_data]= next_node
        else:
            node = station_id[data]
            node.next = self.head
            self.head.prev = node
    
    def build_next(self, current, data):    #다음역 개설
        output.append(str(current.next.data))
        new_node = Node(data)
        new_node.next = current.next    #역 연결
        current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
        station_id[data] = new_node

    def build_prev(self, current, data):    #이전 역 개설
        output.append(str(current.prev.data))
        new_node = Node(data)
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        new_node.next = current
        station_id[data] = new_node


    def clear_next(self, current):  #다음역 폐쇄
        next_node = current.next    
        output.append(str(next_node.data))
        current.next = next_node.next
        next_node.next.prev = current
        next_node = None

    def clear_prev(self, current):  #이전역 폐쇄
        prev_node = current.prev
        output.append(str(prev_node.data))
        current.prev = prev_node.prev
        prev_node.prev.next = current
        prev_node = None


N, M = map(int, input().split())
nums = list(map(int, input().split()))
station_id = {}
stations = LinkedList()

for i in range(len(nums)):
    if i != len(nums) -1:
        stations.append(nums[i], nums[i+1])
    else:
        stations.append(nums[i], None)

for _ in range(M):
    commands = list(input().split())
    command = commands[0]
    if command == "BN":
        station = station_id[int(commands[1])]
        stations.build_next(station, int(commands[2]))
    elif command == "BP":
        station = station_id[int(commands[1])]
        stations.build_prev(station, int(commands[2]))
    elif command == "CN":
        station = station_id[int(commands[1])]
        stations.clear_next(station)
    elif command == "CP":
        station = station_id[int(commands[1])]
        stations.clear_prev(station)
    else:
        print("wrong command")
sys.stdout.write("\n".join(output))