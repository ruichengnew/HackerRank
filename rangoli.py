n = int(input())
A = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1,n+1):
    w = "-".join(A[n-i:n])
    e = w[1:][::-1]
    print((e + w).center(4*n-3, "-"))
for i in range(1, n):
    q = '-'.join(A[i:n])
    r = q[1:][::-1]
    print((r + q).center(4*n-3, '-'))
