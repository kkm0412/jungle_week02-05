# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
ip = ['0000' for i in range(8)]
inputs = input().split(":")

ip_count = 7
for i in range(ip_count+1, 0, -1):    #뒤부터
    x = inputs.pop() #각 자리별 자리수(0~3)
    num_len = len(x)
    if num_len == 3:
        ip[ip_count] = "0"+x
        pass
    elif num_len == 2:
        ip[ip_count] = "00"+x
        pass
    elif num_len == 1:
        ip[ip_count] = "000"+x
        pass
    elif num_len == 0:
        break
    else:
        ip[ip_count] = x
        pass
    ip_count -= 1
for i in range(0,len(inputs)):   
    x = inputs[i] #각 자리별 자리수(0~3)
    num_len = len(x)
    if num_len == 3:
        ip[i] = "0"+x
        pass
    elif num_len == 2:
        ip[i] = "00"+x
        pass
    elif num_len == 1:
        ip[i] = "000"+x
        pass
    elif num_len == 0:
        break
    else:
        ip[i] = x
        pass
    pass #앞부터
# print(ip)

for i in range(0,7):
    print(ip[i], end=":")
print(ip[7])