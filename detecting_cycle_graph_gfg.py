
# Driver Program
def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

def isCyclic(n, graph):
    for source in list(graph):
        visited = [False] * n
        visited[source] = True
        
        if isCyclicRec(graph, source, visited):
            return True
            
    return False

def isCyclicRec(graph, source, visited):
    flag = 0
    for i in graph[source]:
        if visited[i] == True:
            return True
        else:
            visited[i] = True
            if isCyclicRec(graph, i, visited):
                flag = 1
    if flag == 1:
        return True
    
    return False   

from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)

"""
def dfsutil(v, recs, visit, graph):
    if visit[v] is False:
        visit[v]=True
        recs[v]=True
        for i in graph[v]:
            if not visit[i] and dfsutil(i, recs, visit, graph):
                return True
            elif recs[i]:
                return True
    recs[v]=False
    return False

def isCyclic(n, graph):
    # Code here
    visit = [False] * n
    recs = [False] * n
    for i in range(n):
        if visit[i]==False:
            if dfsutil(i, recs, visit, graph) is True:
                return True
    return False
"""   