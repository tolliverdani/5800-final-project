from components import Graph, Node
from data import API, CSV
from model.CostAnalysis import *

bus_csv = './data/MBTA_Bus_Distances.csv'

MBTA = Graph.Graph()


# function to add station nodes to graph - O(n + k)
def add_nodes_to_graph(MBTA_data, bus_data):
    # loop through the API data and
    # save the nodes in the graph
    for station in MBTA_data['features']:
        # initializing a node
        source = Node.Node(station['properties']['from_station_name'])
        source.addColor(station['properties']['route_id'])

        # & saving it to the graph
        MBTA.addNode(source)

    # loop through the CSV data and
    # save the nodes in the graph
    for station in bus_data:
        # initializing a node
        source = Node.Node(bus_data[station]['from_station_name'])
        source.addColor(bus_data[station]['\ufeffroute_id'])

        # & saving it to the graph
        MBTA.addNode(source)


def add_edges_to_nodes(data, bus_data):
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
        MBTA.addEdges(source, dest, color, weight)

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
        MBTA.addEdges(source, dest, color, weight)


# main function to run the program
if __name__ == '__main__':
    # getting the station data
    station_data = API.get_station_response()
    bus_data = CSV.get_bus_data(bus_csv)

    # adding nodes & edges
    add_nodes_to_graph(station_data, bus_data)
    add_edges_to_nodes(station_data, bus_data)

    # default input values for testing
    print("\n## SELECT STARTING STATION ##")
    START = MBTA.select_station()

    print("\n## SELECT END STATION ##")
    END = MBTA.select_station()

    # run the distances using nested loops
    distances = MBTA.shortest_path(START)
    MBTA.print_path(START, END, distances)

    # run the distances using heap
    distances2 = MBTA.shortest_path_heap(START)
    MBTA.print_path(START, END, distances2)

    print("Total Distance from " + START + " to " + END + " = " + str(round(distances[END]["weight"], 2)) + " miles.")

    runCalc(distances, START, END)
