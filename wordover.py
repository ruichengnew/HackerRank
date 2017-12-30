#version 1
#有些built-in的东西可以自己写出来，不过得多看多记多学
#世界上早就有厉害的程序员写出了完美的代码，我只需要去拿来用就好了。
from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    item = input()
    d[item] = d.get(item, 0) + 1

print(len(d.keys()))
print(*d.values())

#version 2
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
