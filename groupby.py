#新老程序的对比

#version 1
#其实，看itertools的时候，就觉得，这些module和method都是人写出来的，所有的def什么的都可以被重新写一遍，想着自己应该也能创造一些函数出来，所以刚看到这个题的时候就想着自己不用你推荐的函数，也一个一样的出来，就写了
#但是，最后看了discussion，觉得自己很蠢，那么简单的一句话，自己硬是要多花几倍的时间去处理，凸显一个无知与傲慢
#再说回来，这也是一个小测试吧，自己学了东西，如果都用不出来，不是很傻，在这个代码我就用了break，双重计数，end不换行，以及format格式转换，这些可能对于高手来说稀疏平常，但是用出来的时候还是爽了一下
#最后还是希望加油吧
def num(count, l):
    count = 1
    while count <= len(l):
        amount = 1
        for i in range(count - 1, len(l)):
            if i + 1 <= len(l) - 1 and l[i+1] == l[i]:
                amount += 1
                count += 1
            else:
                print('({}, {})'.format(amount, l[i]), end = ' ')
                count += 1
                break


l = list(str(input()))
num(l)


#version 2
#一行用groupby
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
