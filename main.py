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
        station_name = station['properties']['from_station_name']
        line_color = station['properties']['route_id']
        # initializing a node
        node = Node.Node(station_name)

        # & saving it to the graph
        MBTA.addNode(node, line_color)


# function to add edges to graph - O(n + k)
def add_edges_to_graph(station_data):
    # loop through the API data and
    # save the edges in the graph
    for station in station_data['features']:
        # adding the edge between nodes
        MBTA.addEdge(station['properties']['to_station_name'],  # source station name
                     station['properties']['from_station_name'],  # dest station name
                     station['properties']['distance_between_miles']  # distance
                     )


# main function to run the program
if __name__ == '__main__':
    MBTA.print()

    # getting the station data
    station_data = API.get_station_response()

    # adding nodes
    add_nodes_to_graph(station_data)

    # adding edges
    add_edges_to_graph(station_data)

    print(MBTA.getKeys())
    print(MBTA.getStation("Porter"))

    MBTA.print()