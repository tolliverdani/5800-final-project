from collections import defaultdict
from components import Node


class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict()

        # what if we store a nodes list that has {name:node}
        self.nodes = defaultdict()

        # store route combos for user selection
        self.station_routes = defaultdict()

    # function to add a node to the graph
    def addNode(self, node: Node.Node(str)):
        if node.station not in self.graph:
            self.graph[node.station] = node
        else:
            self.getStation(node.station).addColor(node.color)

    # function to add edges to the graph
    def addEdges(self, source: str, dest: str, color: str, weight: float):
        # look up the nodes
        source_node = self.graph[source]
        dest_node = self.graph[dest]

        # then define the edges
        source_node.addEdge(dest_node.station, color, weight)

        # add color / station to station_routes dictionary
        if color not in self.station_routes.keys():
            # first time adding this color, then add both
            self.station_routes[color] = [source_node.station, dest_node.station]
        else:
            if source_node.station not in self.station_routes[color]:
                self.station_routes[color].append(source_node.station)

            if dest_node.station not in self.station_routes[color]:
                self.station_routes[color].append(dest_node.station)

    # function to return the nodes in graph
    def getKeys(self):
        return self.graph.keys()

    # function to return specific station
    def getStation(self, station):
        return self.graph[station]

    # function to get the edges for a station in the graph dict
    def getEdges(self, station):
        return self.graph[station].edges

    # function to get distance from two stations in the graph dict
    def getDistance(self, source, dest):
        return self.graph[source].edges[dest]
