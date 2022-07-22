from collections import defaultdict

import Node


# graph class to store the graph and graph functions
class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict(dict)

    # function to add a node
    def addNode(self, node: Node.Node(str, str)):
        if not self.graph[node]:
            self.graph[node]

    # function to create an edge between nodes & stores the weight
    def addEdge(self,
                source_node: Node.Node(str, str),
                dest_node: Node.Node(str, str),
                weight: int):
        self.graph[source_node][dest_node] = weight
        self.graph[dest_node][source_node] = weight

    # function to print the graph
    def print(self):
        for vertex in self.graph.items():
            print(str(vertex))
