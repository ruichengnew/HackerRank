# You should think more about the computation.

#version 1
K = int(input())
l = list(input().split())

for i in set(l):
    if l.count(i) == 1:
        print(i)

#version 2
l = input() == 0 or input().split()
print([i for i in set(l) if list(l).count(i) == 1])

#version 3
# a new type of computation
K = int(input())
l = list(map(int, input().split()))

print((K * sum(set(l)) - sum(l))//(K - 1))

#version 4
# another new type of computation
K = int(input())
l = list(map(int, input().split()))
s1 = set()
s2 = set()

for i in l:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)

s3 = s1 - s2
print(list(s3)[0])
