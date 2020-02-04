import sys

# recursive
def ways(l, n, s):
    if s == 0:
        return 1
    
    if s < 0:
        return 0
    
    if n <= 0 and s >= 1:
        return 0
    
    return ways(l, n-1, s) + ways(l, n, s-l[n-1])

# recursive min number of coins
def min_coins_needed(l, s):
    if s == 0:
        return 0
    ans = sys.maxsize
    for i in l:
        if s >= i:
            t_ans = min_coins_needed(l, s-i)
            if t_ans != sys.maxsize and t_ans + 1 < ans:
                ans = t_ans + 1
    return ans
            

l = [1, 7, 10]
s = 15
print(min_coins_needed(l, s))
    
for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    s = int(input())
    
    print(ways(l, n, s))