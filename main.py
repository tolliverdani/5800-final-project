# importing class files
import Node
import Graph
import API

MBTA = Graph.Graph()


# function to add edges to graph - O(n + k)
def add_edges_to_graph2(station_data):
    # loop through the API data and
    # save the nodes in the graph
    for station in station_data['features']:
        # initializing the source node
        source_node = Node.Node(
            station['properties']['from_station_name']  # station name
        )
        # TODO: need help getting this to actually check the nodes
        #  and prevent repeats
        if MBTA.inGraph(source_node):
            print("source NOT " + str(MBTA[source_node]))
            MBTA.addNode(source_node)

        # initializing the dest node
        dest_node = Node.Node(
            station['properties']['to_station_name']  # station name
        )
        # TODO: need help getting this to actually check the nodes
        #  and prevent repeats
        if MBTA.inGraph(dest_node):
            print("dest NOT " + str(MBTA[source_node]))
            MBTA.addNode(dest_node)

        # adding the edge between nodes
        MBTA.addEdge(source_node,
                     dest_node,
                     station['properties']['distance_between_miles']
                     )


# function to add station nodes to graph - O(n + k)
def add_nodes_to_graph(station_data):
    # loop through the API data and
    # save the nodes in the graph
    for station in station_data['features']:
        # initializing a node
        node = Node.Node(
            station['properties']['from_station_name'],  # station name
            station['properties']['route_id']  # line color
        )
        # & saving it to the graph
        MBTA.addNode(node)


# function to add edges to graph - O(n + k)
def add_edges_to_graph(station_data):
    # loop through the API data and
    # save the edges in the graph
    for station in station_data['features']:
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
    station_data = API.get_station_response()

    # adding nodes
    add_edges_to_graph2(station_data)
    MBTA.print()

    # adding edges
    # add_edges_to_graph(station_data)
    # MBTA.print()
