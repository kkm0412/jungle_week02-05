# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
# 문자열을 대문자의 문자 배열로 바꾸고
# 딕셔너리에 저장

#1 초기 버전
# txt = str(input()).upper()
# letters = list(txt)

# alphabets ={}
# for letter in letters:
#     if letter in alphabets:
#         alphabets[letter] += 1
#     else:
#         alphabets[letter] = 1
# # print(alphabets)
# check = 0
# check_alphabet = None
# for x in alphabets:

#     if check == alphabets[x]:
#         check_alphabet = "?"
#     elif check < alphabets[x]:
#         check = alphabets[x]
#         check_alphabet = x
# if check_alphabet == "x":
#     print("?")
# else:
#     print(check_alphabet)

#2 최적화(문자열 .count() 사용)
txt = str(input()).upper()
alphabets = set(list(txt))

# print(alphabets)
count_num = 0
count_alpha = None
for alphabet in alphabets:
    x = txt.count(alphabet)
    if count_num < x:
        count_num = x
        count_alpha = alphabet
    elif count_num == x:
        count_alpha = "?"

print(count_alpha)

# 기존 208ms -> 80ms