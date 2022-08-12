from components import Graph, Node
from data import API, CSV

bus_csv = './data/MBTA_Bus_Distances.csv'


# function to add station nodes to graph - O(n + k)
def add_nodes_to_graph(MBTA_data, bus_data, graph):
    # loop through the API data and
    # save the nodes in the graph
    for station in MBTA_data['features']:
        # initializing a node
        source = Node.Node(station['properties']['from_station_name'])
        source.addColor(station['properties']['route_id'])

        # & saving it to the graph
        graph.addNode(source)

    # loop through the CSV data and
    # save the nodes in the graph
    for station in bus_data:
        # initializing a node
        source = Node.Node(bus_data[station]['from_station_name'])
        source.addColor(bus_data[station]['\ufeffroute_id'])

        # & saving it to the graph
        graph.addNode(source)


def add_edges_to_nodes(data, bus_data, graph):
    # loop through the API data and
    # save the edges in the nodes
    for station in data['features']:
        # initializing the weight
        weight = station['properties']['distance_between_miles']

        # defining the two stations
        source = station['properties']['from_station_name']
        dest = station['properties']['to_station_name']
        color = station['properties']['route_id']

        # adding the edge between nodes
        graph.addEdges(source, dest, color, weight)

    # loop through the CSV data and
    # save the nodes in the graph
    for station in bus_data:
        # initializing the weight
        weight = float(bus_data[station]['distance_between_miles'])

        # defining the two stations
        source = bus_data[station]['from_station_name']
        dest = bus_data[station]['to_station_name']
        color = bus_data[station]['\ufeffroute_id']

        # adding the edge between nodes
        graph.addEdges(source, dest, color, weight)


def build_graph():
    graph = Graph.Graph()

    # getting the station data
    station_data = API.get_station_response()
    bus_data = CSV.get_bus_data(bus_csv)

    # adding nodes & edges
    add_nodes_to_graph(station_data, bus_data, graph)
    add_edges_to_nodes(station_data, bus_data, graph)

    return graph
