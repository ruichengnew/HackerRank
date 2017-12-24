#This file records the Minion Game

#version 1
#Not good one, I made a stupid mistake
S = input()
counts = 0
for i in ['A', 'E', 'O', 'I', 'U']:
    for j in range(0, len(S)):
        if S[j] == i:
            S = S.replace(S[j], 'Q', 1)
            counts = counts + len(S) - j
Kevin = counts
Stuart = len(S)*(len(S)+1)/2 - Kevin
if Stuart > Kevin:
    print("Stuart", int(Stuart))
elif Stuart < Kevin:
    print("Kevin", int(Kevin))
else:
    print("Draw")

#version 2
S = input()
Kevin = 0
Stuart = 0

for i in range(0, len(S)):
    if S[i] in ['A', 'E', 'O', 'I', 'U']:
        Kevin += len(S) - i
    else:
        Stuart += len(S) - i

if Stuart > Kevin:
    print("Stuart", int(Stuart))
elif Stuart < Kevin:
    print("Kevin", int(Kevin))
else:
    print("Draw")
