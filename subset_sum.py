l = [5, 10, 12, 13, 15, 18]
ans = []
def find_subsets(l, count, sum):
    print(count, sum)
    if sum == 30:
        print('Yes')
    
    if count >= len(l):
        return
    
    if sum+l[count] > 30:
        return
    
    #ans.append()
    
    find_subsets(l, count+1, sum+l[count])
    find_subsets(l, count+1, sum)
    
def find_subsets_2(l, count, sum):
    
    if sum == 30:
        return 1
    
    if count >= len(l):
        return 0
    
    if sum+l[count] > 30:
        return 0
    
    return find_subsets_2(l, count+1, sum+l[count]) + find_subsets_2(l, count+1, sum)

find_subsets_2(l, 0, 0)

#l = [5, 10, 12, 13, 15, 18]
#ans = []
#def find_subsets(l, count, sum):
#    print(count, sum)
#    if sum == 30:
#        print('Yes')
#    
#    if count >= len(l):
#        return
#    
#    if sum+l[count] > 30:
#        return
#    
#    find_subsets(l, count+1, sum+l[count])
#    find_subsets(l, count+1, sum)
#
#find_subsets(l, 0, 0)