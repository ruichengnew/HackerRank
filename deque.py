

#version 1
#我的
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    l = input().split()
    if len(l) == 2:
        getattr(d, l[0])(int(l[1]))
    else:
        getattr(d, l[0])()

print(*d)

#version 2
#简化的
from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*d)
