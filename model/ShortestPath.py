from cmath import inf
import heapq as hq
import time


# function to create copy of graph as a dictionary to keep track of distances between nodes
# key = station, weight = as described, prev = previous station, color = color of the line
def create_distance_dictionary(graph, source: str):
    # create an empty dictionary
    d_nodes = {}

    # initialize all values as infinity (except the source = 0)
    for key in graph.graph.keys():
        if key == source:
            d_nodes[key] = {"weight": 0, "prev": key, "color": ""}
        else:
            d_nodes[key] = {"weight": inf, "prev": "", "color": ""}

    # return the dict
    return d_nodes


# function to create a tuple representation of the graph that holdes (distance, station)
# so that the heapq can be used
def create_distance_tuple(graph, source: str):
    # create an empty dictionary
    d_nodes = []

    # initialize all values as infinity (except the source = 0)
    for key in graph.graph.keys():
        if key == source:
            d_nodes.append((0, key))
        else:
            d_nodes.append((inf, key))

    # return the dict
    return d_nodes


# helper function to create a visited dict
# this helps to keep track of which nodes have been visited
def create_visited_dictionary(graph):
    # create an empty dict
    d_nodes = {}

    # initialize all values as false
    for key in graph.graph.keys():
        d_nodes[key] = False

    # return the dict
    return d_nodes


# this is a shortest_path algorithm that uses a min heap via the heapq library
def shortest_path_heap(graph, source: str):
    # capture start time
    start_time = time.time()

    # create visited dictionary, distance dictionary, and a min heap
    visited_dict = create_visited_dictionary(graph)
    distance_dict = create_distance_dictionary(graph, source)
    min_heap = create_distance_tuple(graph, source)
    hq.heapify(min_heap)

    # while the min_heap isn't empty, pop off the next station with the next smallest distance
    while (len(min_heap) > 0):

        distance, source = hq.heappop(min_heap)

        # if this node has already been visited, skip it and continue
        if (visited_dict[source] == True):
            continue

        # this node is now visited, so update the dictionary
        visited_dict[source] = True

        # retrieve the neighbors of the node that was just removed from the heap
        neighbors = graph.graph[source].edges

        # and iterate over them
        for edge in neighbors:
            key = edge[0]
            color = edge[1]
            weight = edge[2]

            if distance_dict[source]["weight"] + weight == distance_dict[key]["weight"] \
                    and distance_dict[source]["color"] == color:
                # override the value in the dict and save the details
                distance_dict[key]["weight"] = distance_dict[source]["weight"] + weight
                distance_dict[key]["prev"] = source
                distance_dict[key]["color"] = color

                # update the heap with the new value
                hq.heappush(min_heap, (distance_dict[key]["weight"], key))

            # if the distance of the source + weight < what's stored in the dict already
            elif distance_dict[source]["weight"] + weight < distance_dict[key]["weight"]:
                # override the value in the dict and save the details
                distance_dict[key]["weight"] = distance_dict[source]["weight"] + weight
                distance_dict[key]["prev"] = source
                distance_dict[key]["color"] = color

                # update the heap with the new value
                hq.heappush(min_heap, (distance_dict[key]["weight"], key))

    # capture the end time
    end_time = time.time()

    # print total elapsed time
    print("\n--> time elapsed: " + str(end_time - start_time))

    # return distance dictionary, which has shortest path to every station from source
    return distance_dict


# function to calculate the shortest path using a loop to find the next shortest station
def shortest_path(graph, source: str):
    # capture start time
    start_time = time.time()

    # use helper functions to create two dicts, one to track visited nodes and the other to track
    # weights and previous nodes
    visited_dict = create_visited_dictionary(graph)
    distance_dict = create_distance_dictionary(graph, source)

    # iterate over the nodes in the graph
    for i in range(len(graph.graph.items())):

        source = None

        # use a for loop to find the next smallest weight of an unvisited node
        for key_j in graph.graph.keys():
            if not visited_dict[key_j] and (
                    source is None or distance_dict[key_j]["weight"] < distance_dict[source]["weight"]):
                source = key_j

        # mark the source as visited / true
        visited_dict[source] = True

        # get all of the edges from the source node
        neighbors = graph.graph[source].edges

        # and iterate over them
        for edge in neighbors:
            key = edge[0]
            color = edge[1]
            weight = edge[2]

            # if the distance of the source + weight < what's stored in the dict already
            if distance_dict[source]["weight"] + weight < distance_dict[key]["weight"]:
                # override the value in the dict and save the details
                distance_dict[key]["weight"] = distance_dict[source]["weight"] + weight
                distance_dict[key]["prev"] = source
                distance_dict[key]["color"] = color

    end_time = time.time()
    print("\n--> time elapsed: " + str(end_time - start_time))

    # return the final dict
    return distance_dict


def select_station(graph, string: str):
    print("\n## SELECT " + string + "ING STATION ##")
    print("Select the route on which your stop is located. Here are the available routes:")
    for keys in graph.station_routes.keys():
        print(keys)

    print()

    color = input("Type the route name: ")
    while True:
        if color not in graph.station_routes.keys():
            color = input("\n!! That is not valid. Try again: ")
        else:
            break

    print("\nSelect the station. Here are the available stations:")
    for stations in graph.station_routes[color]:
        print(stations)
    print()

    station = input("Type the station name: ")
    while True:
        if station not in graph.station_routes[color]:
            station = input("\n!! That is not valid. Try again: ")
        else:
            break

    return station


# function to print the path from the source to the dest
def print_path(source: str, dest: str, distance_dict):
    # base case: source = dest
    if source == dest:
        print("You are already at your end destination!")
        return

    prev = dest
    color = distance_dict[dest]['color']
    path = []

    while True:
        path.append((prev, color))
        prev = distance_dict[prev]['prev']
        color = distance_dict[prev]['color']
        if prev == source:
            break

    print("## HERE IS YOUR ROUTE ##")
    print("Start at " + source)
    for station in reversed(path):
        print(station[1] + " to ", end="")
        print(station[0])
