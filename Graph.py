from collections import defaultdict

import Node


# graph class to store the graph and graph functions
class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict(dict)

    # function to add a node
    def addNode(self, node: Node.Node(str), color: str):
        if node not in self.graph:
            node.addColor(color)
            self.graph[node.station] = {}

    # function to create an edge between nodes & stores the weight
    def addEdge(self,
                source_node,
                dest_node,
                weight: int):
        source = self.getStation(source_node)
        dest = self.getStation(dest_node)
        source[dest_node] = weight
        dest[source_node] = weight

    # function to return the nodes in graph
    def getKeys(self):
        return self.graph.keys()

    # function to return specific station
    def getStation(self, station):
        return self.graph[station]

    # function to print the graph
    def print(self):
        for station in self.graph:
            print(str(station) + ", " + str(self.graph.get(station)))
        #print(self.graph.items())
