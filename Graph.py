from collections import defaultdict

import Node


# graph class to store the graph and graph functions
class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict()

    # function to add a node
    def addNode(self, node: Node.Node(str)):
        if node.station not in self.graph:
            self.graph[node.station] = node

    def addEdges(self, source: str, dest: str, weight: int):
        # look up the nodes
        source_node = self.graph[source]
        dest_node = self.graph[dest]

        # then define the edges
        source_node.addEdge(dest_node.station, weight)

    # function to return the nodes in graph
    def getKeys(self):
        return self.graph.keys()

    # function to return specific station
    def getStation(self, station):
        return self.graph[station]

    def getEdges(self, station):
        return self.graph[station].edges

    def getDistance(self, source, dest):
        return self.graph[source].edges[dest]

    # TODO: this is just some random chunks of code mushed
    #  together and is not working
    # function to find the shortest path from one
    # station to another
    def findShortestPath(self, source, dest):
        visited = []
        queue = [[source]]

        while queue:

            # look at the node
            for node in self.graph:
                if node not in visited:
                    visited.append(node)

                # look at its edges
                for edge in self.getEdges(node):
                    """print("from "
                          + node + " to "
                          + edge + " "
                          + str(self.getDistance(node, edge)))"""



        return visited
