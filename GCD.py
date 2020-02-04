import math
def gcd(a, b):
    s = a + b
    bigger = a if a > b else b
    smaller = s - bigger
    
    while bigger % smaller != 0:
        temp = bigger % smaller
        bigger = smaller
        smaller = temp
    
    return smaller

print(gcd(60, 48))
print(math.gcd(4, 8))