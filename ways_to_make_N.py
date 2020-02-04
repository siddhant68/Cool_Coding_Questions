def ways(n, cur, l):
    if n == 0:
        return 1
    
    if cur == 0:
        return 0
    
    if n < l[cur-1]:
        return ways(n, cur-1, l)
    
    return ways(n-l[cur-1], cur, l) + ways(n, cur-1, l)

n = 4
l = [x for x in range(1, n)]
print(ways(n, len(l), l))
