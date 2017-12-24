# This file to record the problem "find a string"

#version 1
S, sub = input(), input()
counts = 0
for i in range(0, len(S)-len(sub)+1):
    if S[i:i+len(sub)] == sub:
        counts += 1
print(counts)

#one line maybe
sum[1 for i in range(0, len(S)-len(sub)+1) if S[i:i+len(sub)] == sub]

#version 2


while sub in S:
    i = S.find(sub)
    S = S[:i] + S[i + 1:]
    counts += 1

print(counts)
