# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit( 10 **6)

nums = []

while True: #정해진 입력값 개수가 없어서 예외처리 사용
    try:
        x = int(input())
        nums.append(x)
    except:
        break

def post_order(start, end):
    point = end+1 #start보다 큰값 안나오면 전부 left로 보내기 위해 end+1로 고정
    if start > end:
        return
    if start == end:
        print(nums[start])
        return
    for i in range(start +1, end+1):
        if nums[start] < nums[i]:
            point = i
            break 
    post_order(start+1, point-1)
    post_order(point, end)      
    print(nums[start])

post_order(0, len(nums)-1)


# def post_order(nums, pivot):
#     left_nums =[]
#     right_nums = []
#     for i in range(1, len(nums)):
#         num = nums[i]
#         if num < pivot:
#             left_nums.append(num)
#         else:
#             right_nums.append(num)
#     if len(left_nums) !=0:
#         post_order(left_nums, left_nums[0])
#     if len(right_nums) != 0:
#         post_order(right_nums,  right_nums[0])
#     print(pivot)

# post_order(nums, nums[0])

# 완전 이진트리일때만 효과 있음
# N = [None] * 100000  #노드 수 10000개 이하
# def preorder_put(n, i): #n이 트리순서, i가 nums 순서. 전위순회 입력
#     if i == len(nums):
#         return
#     if N[n] == None:
#         N[n] = nums[i]
#         return
   
#     if nums[i] < N[n]:
#         preorder_put(2 * n, i)
#     else:
#         preorder_put(2 * n + 1, i)

# def postorder_pull(n):  #후위 순회 출력
#     if N[n] == None:
#         return
#     postorder_pull(2 * n)
#     postorder_pull(2 * n + 1)
#     print(N[n])

#맞기는 맞는데 백준에서 터짐 압력도 bst, 출력도 bst면 어쩔수 없음
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def preorder_put(root, num):
#     if root.data > num:
#         if root.left != None:
#             preorder_put(root.left, num)
#         else:
#             root.left = Node(num)
#     else:
#         if root.right != None:
#             preorder_put(root.right, num)
#         else:
#             root.right = Node(num)

# root = Node(nums[0])

# for i in range(1, len(nums)):
#     preorder_put(root, nums[i])

# def postorder_pull(root):
#     if root.left != None:
#         postorder_pull(root.left)
#     if root.right != None:
#         postorder_pull(root.right)
#     print(root.data)


# postorder_pull(root)
########################3
#딕셔너리 방식으로

# tree = {}
# tree[1] = nums[0]

# def preorder_put(i,num):
#     if tree[i] > num:
#         if 2 *i in tree.keys():
#             preorder_put( 2 * i, num)
#         else:
#             tree[2 * i] = num
#     else:
#         if 2 * i + 1 in tree.keys():
#             preorder_put(2 * i + 1, num)
#         else:
#             tree[2 * i + 1] = num

# for i in range(1, len(nums)):
#     preorder_put(1, nums[i])

# def postorder_pull(i):
#     if 2 * i in tree.keys():
#         postorder_pull(2 * i)
#     if 2 * i + 1 in tree.keys():
#         postorder_pull(2 * i + 1)
#     print(tree[i])

# postorder_pull(1)