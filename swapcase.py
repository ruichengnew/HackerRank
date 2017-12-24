#This file is to record the way to code "swap case"

#version 1
s = input()
x = []
for i in s:
    if i.isupper():
        i = i.lower()
        x.append(i)
    else:
        i = i.upper()
        x.append(i)

str1 = "".join(x)

print(str1)

#version 2
print(*map(lambda ch: ch.lower() if ch.isupper() else ch.upper(), input()), sep = "")
#in this line, * means splat operater, which means >>>l = [1, 2, 3, 4, 5]  >>>print(*l)    1 2 3 4 5

#version 3
s = input()
s.swapcase()

#version 4
print ("".join(i.lower() if i.isupper() else i.upper(), for i in input()))
