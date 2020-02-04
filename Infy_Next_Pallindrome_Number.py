n = int(input()) + 1

def pallindrome(n):
    temp = n
    sum = ''
    while temp > 0:
        sum += str(temp % 10)
        temp = temp // 10
    
    if int(sum) == n:
        return True
    
    return False

bool = pallindrome(n)
while not pallindrome(n):
    n += 1

print(n)