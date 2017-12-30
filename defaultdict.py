from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i + 1)
    
for _ in range(m):
    a = input()
    if a in d.keys():
        print(' '.join(map(str, d[a])))
    else:
        print(-1)
