class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, src, dest):
        # UNDIRECTED GRAPH
        
        # Source to Destination
        if src not in self.graph.keys():
            self.graph[src] = []
            self.graph[src].append(dest)
            
        elif dest not in self.graph[src]:
            self.graph[src].append(dest)
        
        # Destination to Source
        if dest not in self.graph.keys():
            self.graph[dest] = []
            self.graph[dest].append(src)
            
        elif src not in self.graph[dest]:
            self.graph[dest].append(src)
    
    def display(self):
        print(self.graph)
        
    def bfs(self, source):
        visited = {}
        
        for i in self.graph.keys():
            visited[i] = False
    
        queue = []
        
        if source not in self.graph.keys():
            print("Invalid key entered")
            return
        
        queue.append(source)
        visited[source] = True
        
        while len(queue) != 0:
            ele = queue.pop(0)
            print(ele, end=' ')
            
            for i in self.graph[ele]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                
    def dfs(self, source):
        visited = {}
        for i in self.graph.keys():
            visited[i] = False
        
        self.__dfs_rec(source, visited)
    
    def __dfs_rec(self, source, visited):
        visited[source] = True
        print(source, end=' ')
        
        for i in self.graph[source]:
            if not visited[i]:
                self.__dfs_rec(i, visited)
                
                
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)        
g.add_edge(1, 2)        
g.add_edge(2, 0)        
g.add_edge(2, 3) 
g.add_edge(3, 3) 
 
g.display()
g.bfs(2)
print()
g.dfs(0)
