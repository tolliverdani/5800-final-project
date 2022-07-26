# importing class files
import Node
import Graph
import API

MBTA = Graph.Graph()


# function to add station nodes to graph - O(n + k)
def add_nodes_to_graph(station_data):
    # loop through the API data and
    # save the nodes in the graph
    for station in station_data['features']:
        # initializing a node
        source = Node.Node(station['properties']['from_station_name'])
        source.addColor(station['properties']['route_id'])

        # & saving it to the graph
        MBTA.addNode(source)


def add_edges_to_nodes(station_data):
    # loop through the API data and
    # save the edges in the nodes
    for station in station_data['features']:
        # initializing the weight
        weight = station['properties']['distance_between_miles']

        # defining the two stations
        source = station['properties']['from_station_name']
        dest = station['properties']['to_station_name']

        # adding the edge between nodes
        MBTA.addEdges(source, dest, weight)


# main function to run the program
if __name__ == '__main__':
    # getting the station data
    station_data = API.get_station_response()

    # adding nodes & edges
    add_nodes_to_graph(station_data)
    add_edges_to_nodes(station_data)

    # to check graph
    print(MBTA.getStation("Porter"))

    # final print of graph
    print(MBTA.graph)
