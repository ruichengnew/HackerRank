# About one-liner and 'getattr' method

# version 1 set mutation
#there are three problems which are really in the same type. I always write it like this, but there are always anoter more concise way to write code. See version 2.
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd = list(input().split())[0]
    data = set(map(int, input().split()))
    if cmd == 'intersection_update':
        s.intersection_update(data)
    if cmd == 'update':
        s.update(data)
    if cmd == 'symmetric_difference_update':
        s.symmetric_defference_update(data)
    if cmd == 'difference_update':
        s.difference_update(data)

print(sum(s))


#version 2
#the one-liner told me how to make your script easier and more elegant.
S = input() == 0 or set(input().split())
print([getattr(S, input().split()[0])(input().split()) for _ in range(int(input()))] == [] or sum(map(int, S)))
