# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data, current): #연결리스트 초기화용
        if self.head == None:
            self.head = Node(data)
            current.prev = self.head
            self.head.next = current
            return self.head

        else:
            new_node = Node(data)
            current.prev.next = new_node
            new_node.prev = current.prev
            current.prev = new_node
            new_node.next = current


    def left(self, current):    #왼쪽노드로 이동
        if current.prev != None:
            current = current.prev
        return current
    
    def right(self, current):   #오른쪽노드로 이동
        if current.next != None:
            current = current.next
        return current
    
    def delete(self, current):  #현재 위치로 이전 노드 삭제
        if current.prev == None:
            return current
            
        target = current.prev
        current.prev = target.prev
        
        if target.prev != None:
            target.prev.next = current
        else:
            self.head = current
        target.data = None
        target.prev = None
        target.next = None
        return current
        
    def add(self, current, data):   #노드 추가하고 현재랑 이전 노드와 연결
        if current.prev != None:
            target = Node(data)
            current.prev.next = target
            target.prev = current.prev
            current.prev = target
            target.next = current
            # link.printer()
            return current
        else:
            target = Node(data)
            self.head = target
            self.head.next = current
            current.prev = self.head
            return current
    def printer(self):
        node = self.head
        while node.next is not None and node.data is not None:
            print(node.data, end="")
            node = node.next
        # print("붙임")

word = list(input())

link = LinkedList()
cursor = Node(None)

for letter in word:
    link.append(letter, cursor)
    # link.printer()

N = int(input())

for n in range(N):
    inputs = list(input())
    if inputs[0] == 'L':
        cursor = link.left(cursor)    
    elif inputs[0] == 'D':
        cursor = link.right(cursor)
    elif inputs[0] == 'B':
        cursor = link.delete(cursor)
    elif inputs[0] == 'P':
        cursor = link.add(cursor, inputs[2])
link.printer()