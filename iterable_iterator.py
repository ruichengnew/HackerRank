from itertools import combinations

N = int(input())
l = input().split()
K = int(input())

B = len(list(combinations(l, K)))
a = l.count('a')
A = len(list(combinations(l[a:], K)))

print(1 - A / B)
