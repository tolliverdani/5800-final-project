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

    # TODO: below is not a working function - right now it
    #  just iterates over the nodes

    # function to find the shortest path from one
    # station to another
    def findShortestPath(self, source, dest):
        visited = []
        queue = [[source]]
        index = 0

        # to prevent infinite looping
        while index < len(self.graph):

            # iterate over the nodes and their edges
            for node in self.graph:
                if node not in visited:
                    index += 1
                    visited.append(node)

                    # look at its edges & distances
                    for edge in self.getEdges(node):
                        # just printing the data for now
                        print("from "
                              + node + " to "
                              + edge + " "
                              + str(self.getDistance(node, edge)))

        return visited
