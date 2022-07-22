from collections import defaultdict

import requests
import json

# importing class files
import Node
import Graph

import API

MBTA = Graph.Graph()


# function to add station nodes to graph - O(n + k)
def add_nodes_to_graph(data):
    # loop through the API data and
    # save the nodes in the graph
    for station in data['features']:
        # initializing a node
        node = Node.Node(
            station['properties']['from_station_name'],  # station name
            station['properties']['route_id']  # line color
        )
        # & saving it to the graph
        MBTA.addNode(node)


# function to add edges to graph - O(n + k)
def add_edges_to_graph(data):
    # loop through the API data and
    # save the edges in the graph
    for station in data['features']:
        # initializing the source node
        source_node = Node.Node(
            station['properties']['from_station_name'],  # station name
            station['properties']['route_id']  # line color
        )

        # initializing the dest node
        dest_node = Node.Node(
            station['properties']['to_station_name'],  # station name
            station['properties']['route_id']  # line color
        )

        # adding the edge between nodes
        MBTA.addEdge(source_node,
                     dest_node,
                     station['properties']['distance_between_miles']
                     )


# main function to run the program
if __name__ == '__main__':
    # getting the station data
    data = API.get_station_response()

    # graphing functions
    add_nodes_to_graph(data)
    add_edges_to_graph(data)

    # printing to see output
    MBTA.print()
