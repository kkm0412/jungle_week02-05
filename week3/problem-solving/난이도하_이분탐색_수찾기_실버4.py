# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import random

N = int(input())

A = list(map(int, input().split(" ")))

M = int(input())

nums = list(map(int, input().split(" ")))

# print(A)

#먼저 A를 정렬(퀵정렬로)
# 입력 받은 nums로 이진 탐색 하기

# def quick_sort(data, left, right):
#     if left > right:
#         return
#     pivot = data[right]
#     i = left -1
#     j = left
#     while j < right:
#         if data[j] < pivot:
#             i +=1
#             data[i], data[j] = data[j], data[i]
#         j += 1
#     i += 1

#     data[i], data[j] = data[j], data[i]
#     quick_sort(data, left, i -1)
#     quick_sort(data, i+1, right)

# def quick_sort_random(data, left, right):
#     if left >= right:
#         return
#     x = random.randrange(left, right+ 1)
#     pivot = data.pop(x)
#     i = left -1
#     j = left
#     while j < right:
#         if data[j] < pivot:
#             i +=1
#             data[i], data[j] = data[j], data[i]
#         j += 1
#     i += 1

#     data.insert(i, pivot)
#     quick_sort_random(data, left, i -1)
#     quick_sort_random(data, i+1, right)
#   #랜덤 적용시 pop을 하니 배열이 계속 바뀌어서 재귀시 문제생김

# def quick_sort_fix(data, left, right):
#     if left >= right:
#         return
#     x = random.randrange(left, right+ 1)
#     #ㅏ기존 random과 다르게 아예 랜덤한걸 오른쪽으로 옮겨서 생각
#     data[x], data[right] = data[right],data[x] 

#     pivot = data[right]

#     i = left -1
#     j = left
#     while j < right:
#         if data[j] < pivot:
#             i +=1
#             data[i], data[j] = data[j], data[i]
#         j += 1
#     i += 1

#     data[i], data[j] = data[j], data[i]
#     quick_sort_fix(data, left, i -1)
#     quick_sort_fix(data, i+1, right)


def finder(data, left, right, target):
    if left > right:
        return 0

    mid = (left + right) // 2
    if data[mid] == target:
        return 1
    elif data[mid] < target:
        return finder(data, mid+1, right, target)
    else:
        return finder(data, left, mid-1, target)

# 테스트용
# quick_sort(A, 0, N-1)
#quick_sort_fix(A, 0, N-1)
A.sort() #<- 직접 만든 퀵정렬은 타임아웃 나는데 이건 안나네 이런 ㅆ...

# print(A)
for i in nums:
    print(finder(A, 0, N-1, i))

