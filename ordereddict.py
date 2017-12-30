from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)

for k, v in d.items():
    print(k, v)
