from collections import defaultdict

import Node


# graph class to store the graph and graph functions
class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict(dict)

    # function to get an item
    def __getitem__(self, item):
        return item

    # TODO: need help making a function to check
    #  if the item is in the graph
    # function to check if node in graph
    def inGraph(self, node: Node.Node(str)):
        for vertex in self.graph.items():
            print(str(vertex))
            if node == vertex:
                return True
            return False

    # function to add a node
    def addNode(self, node: Node.Node(str)):
        if not self.graph[node]:
            self.graph[node]

    # function to create an edge between nodes & stores the weight
    def addEdge(self,
                source_node: Node.Node(str),
                dest_node: Node.Node(str),
                weight: int):
        self.graph[source_node][dest_node] = weight
        self.graph[dest_node][source_node] = weight


    # function to print the graph
    def print(self):
        for vertex in self.graph.items():
            print(str(vertex))