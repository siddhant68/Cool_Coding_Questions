from itertools import (permutations, combinations
, combinations_with_replacement, accumulate)

import operator

a = [12, 4, 18, 8]
perm = permutations(a)
perm1 = permutations(a, 2)
print(list(perm))
print(list(perm1))

comb = combinations(a, 2)
print(list(comb))

c = combinations_with_replacement(a, 2)
print(list(c))

acc = accumulate(a)
acc2 = accumulate(a, func=operator.mul)
acc3 = accumulate(a, func=max)
print(list(acc), list(acc2), list(acc3))

print(list(filter(lambda x: x % 2, a)))

d = {1: 55, 2: 98, 3: 66}
print(max(d, key=lambda x: d[x]))

s = 'siddhant'
print(list(set(s)))