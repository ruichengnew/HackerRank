#注意更新自己的知识库

#version 1
#变得不喜欢用新东西了，这样不好，得改
X = int(input())
l = input().split()
n = int(input())
money = 0
for _ in range(n):
    l2 = input().split()
    if l2[0] in l:
        money += int(l2[1])
        l.remove(l2[0])
print(money)

#version 2
#新东西确实需要练习， 别人写的很好
from collections import Counter

n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
total = []

for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
		total.append(b)
		s.subtract(Counter([a]))
    else:
        pass

print (sum(total))
