n = int(input())
l = []

for i in range(n):
    lis = list(input().split())
    if lis[0] == "insert":
        l.insert(int(lis[1]), int(lis[2]))
    elif lis[0] == 'sort':
        l.sort()
    elif lis[0] == 'remove':
        l.remove(int(lis[1]))
    elif lis[0] == 'append':
        l.append(int(lis[1]))
    elif lis[0] == 'reverse':
        l.reverse()
    elif lis[0] == 'pop':
        l.pop()
    else:
        print(l)
