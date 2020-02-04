l = [0, 1, 2, 3, 3, 4, 4, 2]
parent = [-1] * (max(l)+1)

def findRec(v, source, count, parent):
    if parent[v] >= 0:
        return findRec(parent[v], source, count+1, parent)
 
    if count > 1:
        parent[source] = v
        return v

    return v

def find(source):
    return findRec(source, source, 0, parent)

def union(p1, p2):
    if parent[p1] <= parent[p2]:
        parent[p1] += parent[p2]
        parent[p2] = p1
    else:
        parent[p2] -= parent[p1]
        parent[p1] = p2


flag = 0
for i in range(0, len(l)-1, 2):
    if find(l[i]) == find(l[i+1]):
        print(find(l[i]), find(l[i+1]))
        flag = 1
        break
    else:
        union(find(l[i]), find(l[i+1]))
    print(parent)
    
if flag == 1:
    print('Cycle Detected, Do something bro!!')
else:
    print('No cycle man, have fun')
