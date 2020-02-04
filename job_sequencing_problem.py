def fit(ans, i):
    temp = i[1]-1
    while temp >= 0:
        if ans[temp] == None:
            ans[temp] = i[0]
            return True
        
        temp -= 1
    return False

for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    l1 = []
    for i in range(0, len(l)-2, 3):
        l1.append([l[i], l[i+1], l[i+2]])
    
    l1.sort(key=lambda x: x[2], reverse=True)
    
    ans = [None] * (max(l1, key=lambda x:x[1])[1])
    
    for i in l1:
        fit(ans, i)
    
    filter = [x for x in ans if x is not None]
    
    profit = 0
    for i in l1:
        if i[0] in filter:
            profit += i[2]
    
    print(len(filter), profit)
