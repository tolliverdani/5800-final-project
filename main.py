from collections import defaultdict

import requests
import json


# node class to store the MBTA station information
class Node:

    # constructor that takes in station name and line color
    def __init__(self, station: str, color: str):
        self.station = station
        self.color = color

    # repr that returns the station name
    def __repr__(self):
        return self.station


# graph class to store the graph and graph functions
class Graph:

    # constructor with no params and creates a dict
    def __init__(self):
        self.graph = defaultdict(dict)

    # function to create an edge between nodes & stores the weight
    def addEdge(self, source_node: Node(str, str), dest_node: Node(str, str), weight: int):
        self.graph[source_node][dest_node] = weight
        self.graph[dest_node][source_node] = weight

    # function to print the graph
    def print(self):
        for vertex in self.graph.items():
            print(str(vertex))


# function to call MBTA station API and pass information in JSON format
def get_station_response():

    # get the response from the third-party API
    response = requests.get(
        "https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/" +
        "rest/services/MBTA_Rapid_Transit_Stop_Distances/Feature" +
        "Server/0/query?outFields=*&where=1%3D1&f=geojson")

    # return the JSON load
    return (json.loads(response.text))


# function to call ridership API and pass information in JSON format
def get_ridership_response():

    # get the response from the third-party API
    response = requests.get(
        "https://services1.arcgis.com/ceiitspzDAHrdGO1/" +
        "arcgis/rest/services/Rail_Ridership_by_Season_Time_Period_" +
        "RouteLine_and_Stop/FeatureServer/0/query?outFields=*&where=" +
        "1%3D1&f=geojson")

    # return the JSON load
    return (json.loads(response.text))


# function to receive ridership JSON and save relevant data in array
def clean_ridership_data(API_data):

    # initialize an empty array
    ridership = []

    # loop through the API data and only save
    # what's needed for our graph
    for station in API_data['features']:
        ridership_details = {"station": station['properties']['stop_name'],
                             "day_type": station['properties']['day_type_name'],
                             "time_period": station['properties']['time_period_name'],
                             "color": station['properties']['route_id'],
                             "average_flow": station['properties']['average_flow']}
        ridership.append(ridership_details)

    # return the array
    return ridership


# function to receive MBTA station JSON and save relevant data in array
def clean_station_data(API_data):

    # initialize an empty array
    MBTA = []

    # loop through the API data and only save
    # what's needed for our graph
    for station in API_data['features']:
        MBTA_details = {"id": station['id'],
                        "source": station['properties']['from_station_name'],
                        "destination": station['properties']['to_station_name'],
                        "color": station['properties']['route_id'],
                        "distance": station['properties']['distance_between_miles']}
        MBTA.append(MBTA_details)

    # return the array
    return MBTA


# helper function to print the MBTA list
def print_array(arr):

    # check the station here
    # check = 'Northeastern University'

    # iterate over the list
    for station in arr:
        # this is just here to check
        # if station['source'] == check or station['destination'] == check:
        # print each station
        # print(station)

        # print each station
        print(station)


# main function to run the program
if __name__ == '__main__':

    #ridership = clean_ridership_data(get_ridership_response())
    # print_array(ridership)

    #MBTA = clean_station_data(get_station_response())
    #print_array(MBTA)

    # TODO: need to push the data from the API into the graph instead of this
    northeastern = Node("Northeastern", "Green")
    copley = Node("Copley", "Green")

    g = Graph()
    g.addEdge(northeastern, copley, 100)

    g.print()