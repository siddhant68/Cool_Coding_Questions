# Recursive Solution 1
def sol_rec(arr, n, summ, calculatedSum):
    global flag
    if n == 0:
        if summ - 2*calculatedSum == 0:
            flag = 'YES'
            return True
        
        else:
            return False
    
    if calculatedSum + arr[n-1] > summ // 2:
        sol_rec(arr, n-1, summ, calculatedSum)
    
    return sol_rec(arr, n-1, summ, calculatedSum) or\
           sol_rec(arr, n-1, summ, calculatedSum + arr[n-1])
          
def sol(arr):
    if sum(arr) % 2 != 0:
        return
    
    sol_rec(arr, len(arr), sum(arr), 0)
    

# Recursive Solution 2
def equal_sub(l, count, calculatedSum):
    if count == len(l):
        if (sum(l)-calculatedSum) - calculatedSum == 0:
            global flag
            flag = 'YES'
        return
    
    equal_sub(l, count+1, calculatedSum+l[count])
    equal_sub(l, count+1, calculatedSum)

for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    
    flag = 'NO'
    sol(l)
    print(flag)
    
    flag = 'NO'
    