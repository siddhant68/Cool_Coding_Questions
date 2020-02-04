class Graph:
    def __init__(self):
        self.g = {}
    
    def add_edge(self, source, destination, weight):
        if source in self.g.keys():
            self.g[source][destination] = weight
        else:
            self.g[source] = {destination: weight}
        
    def display_graph(self):
        print(self.g)
    
    def dijkstra(self, source):
        dist = {}
        for i in self.g.keys():
            dist[i] = 100
        dist[source] = 0
        
        

graph = Graph()
graph.add_edge('a', 'b', 5)
graph.add_edge('a', 'c', 10)
graph.add_edge('b', 'c', 4)
graph.add_edge('b', 'd', 1)
graph.add_edge('c', 'e', 3)
graph.add_edge('d', 'e', 7)
print(len(graph.g))
