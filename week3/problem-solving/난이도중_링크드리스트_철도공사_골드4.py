# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data, is_end): #역 초기화
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.next != None: 
                node = node.next
            node.next = new_node    #역끼리 연결
            new_node.prev = node
        if is_end:  #마지막 역에서 처음 역 연결
            new_node.next = self.head
            self.head.prev = new_node
    
    def find_current(self, current_data):   #고유번호로 역 찾기
        node = self.head
        while node.data != current_data:
            node = node.next
        return node
    
    def build_next(self, current, data):    #다음역 개설
        print(current.next)
        new_node = Node(data)
        new_node.next = current.next    #역 연결
        current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def build_prev(self, current, data):    #이전 역 개설
        print(current.prev)
        new_node = Node(data)
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        new_node.next = current
    def clear_next(self, current):  #다음역 폐쇄
        next_node = current.next    
        print(next_node)
        current.next = next_node.next
        next_node.next.prev = current
        next_node = None

    def clear_prev(self, current):  #이전역 폐쇄
        prev_node = current.prev
        print(prev_node)
        current.prev = prev_node.prev
        prev_node.prev.next = current
        prev_node = None


N, M = map(int, input().split())
nums = list(map(int, input().split()))

stations = LinkedList()

for i in range(len(nums)):
    if i != len(nums):
        stations.append(nums[i], False)
    else:
        stations.append(nums[i], True)

for _ in range(N):
    commands = list(input().split())
    command = commands[0]
    if command == "BN":
        station = stations.find_current(int(commands[1]))
        stations.build_next(station, int(commands[2]))
    elif command == "BP":
        station = stations.find_current(int(commands[1]))
        stations.build_prev(station, int(commands[2]))
    elif command == "CN":
        station = stations.find_current(int(commands[1]))
        stations.clear_next(station)
    elif command == "CP":
        station = stations.find_current(int(commands[1]))
        stations.clear_prev(station)
    else:
        print("wrong command")