#记录了，原始想法，进阶改动，不同思路，可以注意一下

#version 1
#又timeout， 我猜测这次是max这个函数的运行量可能有点大
from collections import deque

n = int(input())

for _ in range(n):
    a = int(input())
    l = deque(map(int, input().split()))
    for i in range(a):
        if i == a - 1:
            print('Yes')
        elif l[0] == max(l):
            l.popleft()
        elif l[-1] == max(l):
            l.pop()
        else:
            print('No')
            break

#version 2
#这个程序有点厉害，看到这个程序我有点明悟，我理解的都是数学的运算，所以会timeout，而这个程序理解的是计算机的运算，所以很流畅！
#awesome
for t in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l - 1 else "No")

#version 3
#更改我的max函数之后的函数
#很有意思的改动，又一次计算机思维的完美体现
from collections import deque

n = int(input())

for _ in range(n):
    a = int(input())
    l = deque(map(int, input().split()))
    for i in reversed(sorted(l)):
        if i == a - 1:
            print('Yes')
        elif l[0] == i:
            l.popleft()
        elif l[-1] == i:
            l.pop()
        else:
            print('No')
            break
