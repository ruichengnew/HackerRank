# This script told me how to use format again, and told me how to use dict.
n = int(input())
dic = {}

for i in range(n):
    s_m = list(input().split())
    dic[s_m[0]] = '{:.2f}'.format((float(s_m[1]) + float(s_m[2]) + float(s_m[3])) / 3)

print(dic[input()])
