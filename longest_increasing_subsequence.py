l = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]

lis = [1] * len(l)

# iterative
def solution(l, lis, j):
    i = 0
    while i < j:
        if l[j] > l[i]:
            lis[j] = max(lis[i]+1, lis[j])
        i += 1
    
    if j+1 < len(l):
        solution(l, lis, j+1)
    else:
        print(max(lis))

# recursive
def solution_rec(l, lis, count):
    if count == len(l):
        return max(lis)
    
    for i in range(count):
        if l[i] < l[count] and lis[i] + 1 > lis[count]:
            lis[count] = lis[i] + 1
    
    return solution_rec(l, lis, count + 1)

solution(l, lis, 1)