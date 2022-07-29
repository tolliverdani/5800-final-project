from cmath import inf
from collections import defaultdict

import Node


# graph class to store the graph and graph functions
class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict()
    
    # function to create copy of graph for dikjstra
    def create_distance_dictionary(self, source: str):
        d_nodes = {}
        for key in self.graph.keys():
            if key == source:
                d_nodes[key] = {"weight": 0, "prev": key}
            else:
                d_nodes[key] = {"weight": inf, "prev": ""}
        
        return d_nodes;
    
    def create_visited_dictionary(self, source: str):
        d_nodes = {}
        for key in self.graph.keys():
            d_nodes[key] = False
        return d_nodes

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

    def print_path(self, source: str, dest: str, distance_dict):
        if ( source == dest ):
            return [source]
        path = []
        path.append(dest)
        prev = distance_dict[dest]['prev']
        
        while (True):
            path.append(prev)
            prev = distance_dict[prev]['prev']
            if ( prev == source ):
                break
        path.append(prev)

        color = None
        for station in reversed(path):
            if ( self.graph[station].color != color ):
                if ( station == source ):
                    print("*** Start on " + self.graph[station].color + " ***")
                else :
                    print("*** Transfer to " + self.graph[station].color + " ***")
            print(station)
            color = self.graph[station].color

            
        

    # TODO: Rather than doing an outer loop, a min_heap would be more efficient
    #       however, I don't see a min heap in Python. Java FTW
    def nate_shortest_path(self, source):

        distance_dict = self.create_distance_dictionary(source)
        visited_dict = self.create_visited_dictionary(source)

        for key_i, value_i in self.graph.items():
            source = None
            for key_j in self.graph.keys():
                if not visited_dict[key_j] and (source == None or distance_dict[key_j]["weight"] < distance_dict[source]["weight"]):
                    source = key_j
            
            if distance_dict[source]["weight"] == inf:
                break

            visited_dict[source] = True
            neighbors = self.graph[source].edges

            for key, value in neighbors.items():
                weight = value
                if ( distance_dict[source]["weight"] + weight < distance_dict[key]["weight"]):
                    distance_dict[key]["weight"] = distance_dict[source]["weight"] + weight
                    distance_dict[key]["prev"] = source

        return distance_dict


            
        
        

        

