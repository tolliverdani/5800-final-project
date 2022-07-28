import csv
import json


# function to call MBTA station API and pass information in JSON format
def get_station_response():
    MBTA = []

    with open('MBTA_Distances.csv', mode='r') as file:
        csvFile = csv.reader(file)

        for lines in csvFile:
            MBTA_details = {"id": lines[4],
                            "source": lines[4],
                            "destination": lines[6],
                            "color": lines[0],
                            "distance": lines[7]}
            MBTA.append(MBTA_details)

    # return the array
    return MBTA


# helper function to print the MBTA list
def print_array(arr):
    # iterate over the list
    for station in arr:
        # print each station
        print("\n" + str(station))


# main function to run the program
if __name__ == '__main__':
    # getting the station & ridership data
    station_data = get_station_response()

    # printing to see output(s)
    print_array(station_data)
