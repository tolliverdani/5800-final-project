from model.components import Graph, Node
from data import API, CSV
from model.CostAnalysis import *

bus_csv = './data/MBTA_Bus_Distances.csv'

MBTA = Graph.Graph()


# TODO: I think we should move these into the model...
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

    # get inputs from controller
    # START, END = getStartEnd()

    # TODO: delete later and use the controller
    # default input values for testing
    print("\n## SELECT STARTING STATION ##")
    START = MBTA.select_station()
    # START = 'Davis'

    print("\n## SELECT END STATION ##")
    END = MBTA.select_station()
    # END = 'Heath Street'



    # print(MBTA.graph)
    # print(MBTA.graph['Ashmont'])
    # TODO: should we refactor all this into the models folder?
    # distances is a hashmap of all stations from the start point
    distances = MBTA.shortest_path(START)
    distances2 = MBTA.shortest_path_heap(START)
    # print(distances)

    # gathers the path from the start to end
    MBTA.print_path(START, END, distances)
    MBTA.print_path(START, END, distances2)
    # print("Total Distance from " + START + " to " + END + " = " + str(round(distances[END]["weight"], 2)) + " miles.")

    # distance calcs go here
    distance = round(distances[END]["weight"], 2)
    cost_per_mile = calculateCost(distance)
    # print(2.70 / distance)
    # print(cost_per_mile)

    # TODO: should we use a plot for the averages for each line?
    #  also we might want to move this to the view
    # https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
    # arr = calculateAllCosts(distances)
    # print(arr)
    # print(calculateAvgCost(distances))
    # plotCalc(arr)
