# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# 리프 늘리는 방법: 기본적으로 리프가 2개 생기므로, 기본적으로 좌측줄기에 잎을 몰아주다가
# m-2개 만큼 리프를 1층부터 우측 줄기에 붙이면 됨 

# class Tree():
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# n, m = map(int, input().split())

# root = Tree(0)

# def append(node, n, is_right):    #node: 현재 줄기, n = 잎의 순번
#     if n != 0 and node.right is None and is_right == True:
#         node.right = Tree(n)
#     elif node.left is not None:
#         append(node.left, n, is_right)
#     else:
#         node.left = Tree(n)
# def show(node, queue):
#     if node.left is not None:
#         queue.append((node.data, node.left.data))
#     if node.right is not None:
#         queue.append((node.data, node.right.data))
#         if node.left is not None:
#             show(node.left, queue)
#         if node.right is not None:
#             show(node.left, queue)
    
    
# leaf_count = m - 2

# for i in range(1, n-1):
#     if leaf_count >0:
#         append(root, i, True)
#         leaf_count -= 1
#     else:
#         append(root, i, False)

# queue = []
# show(root, queue)
# for x in queue:
#     if x[1] is not None:
#         print(x[0], x[1])


n, m = map(int, input().split())

trees = []
for i in range(n-m):
    trees.append((i, i+1))

for x in range(1, m):
    trees.append((n-m, n-m+ x))

for tree in trees:
    print(tree[0], tree[1])
