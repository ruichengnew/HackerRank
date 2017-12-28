
#也有这种粗暴的方法，不闻不问，不想不看，通通给我算出来比大小！
import itertools

k, m = map(int, input().split())

print(max(sum(j) % m for j in itertools.product(*((int(i) ** 2 for i in input().split()[1:]) for _ in range(k)))))
