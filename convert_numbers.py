#This file records the problem "convert numbers"

#vertion 2
n = int(input())
width = len("{0:b}".format(n))
print(hex(n))
for i in range(1,n+1):
  print(("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}").format(i, width=width))

#Vertion 1
n = int(input())
w = len(bin(n)[2:])

for i in range(1, n +1):
    print(str(i).rjust(w), str(oct(i)[2:]).rjust(w), str(hex(i)[2:]).upper().rjust(w), str(bin(i)[2:]).rjust(w))
