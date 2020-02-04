class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, source, destination):
        if source not in self.graph.keys():
            self.graph[source] = []
            self.graph[source].append(destination)
        else:
            self.graph[source].append(destination)
        
        if destination not in self.graph.keys():
            self.graph[destination] = []
            self.graph[destination].append(source)
        else:
            self.graph[destination].append(source)
    
    def display(self):
        print(self.graph)


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

graph.display()

colors = ['red', 'green', 'blue']
graph_colors = {}

def assign_colors(graph, colors, graph_colors, source, visited):
    visited[source] = True
    
    for i in colors:
        if is_color_safe(graph, i, source, graph_colors):
            graph_colors[source] = i
            if len(graph_colors) == len(graph.graph):
                print(graph_colors)
        
            for j in graph.graph[source]:
                if not visited[j]:
                    assign_colors(graph, colors, graph_colors, j, visited)
                    
    visited[source] = False
    
    if source in graph_colors: 
        del graph_colors[source]
    
def is_color_safe(graph, color, source, graph_colors):
    for i in graph.graph[source]:
        if i in graph_colors.keys():
            if graph_colors[i] == color:
                return False
    return True       

visited = {}
for i in graph.graph.keys():
    visited[i] = False
    
assign_colors(graph, colors, graph_colors, 'A', visited)
            