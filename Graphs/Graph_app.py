from Graph import Graph

graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

graph.print_graph()

graph.remove_vertex('D')
graph.print_graph()