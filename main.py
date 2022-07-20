import requests
import json


# function to call MBTA station API and pass information in JSON format
def get_station_response():
    # get the response from the third-party API
    response = requests.get(
        "https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/" +
        "rest/services/MBTA_Rapid_Transit_Stop_Distances/Feature" +
        "Server/0/query?outFields=*&where=1%3D1&f=geojson")

    # & save JSON load in a temp variable
    API_data = json.loads(response.text)

    # return the JSON load
    return (API_data)


# function to call ridership API and pass information in JSON format
def get_ridership_response():
    # get the response from the third-party API
    response = requests.get("https://services1.arcgis.com/ceiitspzDAHrdGO1/" +
                            "arcgis/rest/services/Rail_Ridership_by_Season_Time_Period_" +
                            "RouteLine_and_Stop/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
    # & save JSON load in a temp variable
    API_data = json.loads(response.text)

    # return the JSON load
    return (API_data)


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
        print(ridership_details)

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
    # iterate over the list
    for station in arr:
        # print each station
        print(station)


# main function to run the program
if __name__ == '__main__':
    ridership = clean_ridership_data(get_ridership_response())
    print_array(ridership)

    MBTA = clean_station_data(get_station_response())
    print_array(MBTA)