S = input()
k = int(input())
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for j in range(0, int(len(S)/k)):
    uj = S[j*k:(j+1)*k]

    for i in A:
        tu1, tu2, tu3 = uj.partition(i)
        uj = tu1 + tu2 + tu3.replace(i, '')

    print(uj)
