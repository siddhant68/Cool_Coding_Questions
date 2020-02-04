a, b = map(int, input().split())
treasure = [int(x) for x in input().split()]
color = [int(x) for x in input().split()]

def profit(treasure, color, a, b, col, k):
    sum = 0
    
    if k == len(treasure):
        return 0
    
    if col == color[k]:
        sum += max(a * treasure[k] + profit(treasure, color, a, b, color[k], k+1),
                   profit(treasure, color, a, b, col, k+1))
    else:
        sum += max(b * treasure[k] + profit(treasure, color, a, b, color[k], k+1),
                   profit(treasure, color, a, b, col, k+1))
    
    return sum
    
profit(treasure, color, a , b, 0, 0)