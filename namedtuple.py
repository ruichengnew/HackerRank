#version 1
#我这个方法有几个test case是错误的。。有点迷惑，不知道哪里会出错
n = int(input())
l = input().split()
l3 = []

for i in range(4):
    if l[i] == 'MARKS':
        a = i

for _ in range(n):
    l2 = input().split()
    l3.append(int(l2[a]))

print('{:.2f}'.format(sum(l3)/5))

#version 2
#subclass，class这个东西很有意思，它重新定义了函数，任何一个有class的object都拥有atrribute， 而attribute就是method也就是function，恍恍惚惚
from collections import namedtuple

N = int(input())
fields = input().split()
total = 0
for i in range(N):
    students = namedtuple('student',fields)
    field1, field2, field3,field4 = input().split()
    student = students(field1,field2,field3,field4)
    total += int(student.MARKS)
print('{:.2f}'.format(total/N))
