
#代码简洁清爽，一步到位，我的就不拿出来丢人了。。还要进一步融会贯通对method的理解
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

#模仿写题真的很轻松
from itertools import combinations
s, n = input().split()
print(*[''.join(i) for j in range(1, int(n)+1) for i in combinations(sorted(s), j)], sep = '\n')

#三连发
from itertools import combinations_with_replacement
s, n = input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(s), int(n))], sep = '\n')
