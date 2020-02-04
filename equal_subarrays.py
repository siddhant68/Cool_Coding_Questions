n = int(input())
k = int(input())
l = [int(x) for x in input().split()]

ans = 1

for i in range(len(l)):
    
    if i+ans >= len(l)-1:
        break
    
    maxx = max(l[i: i+ans])
    summ = sum(l[i: i+ans])
    
    for j in range(i+ans, len(l)):
        length = j - i + 1
        maxx = l[j] if l[j] > maxx else maxx
        summ += l[j]
        
        if maxx * length - summ <= k:
            ans = length
        else:
            break

print(ans)