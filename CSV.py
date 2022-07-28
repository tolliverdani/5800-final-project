import csv

# TODO: I think this isn't as useful as the API because it iterates
#  over the entire line and their destinations instead of being
#  station to station figures. LMK.


# function to call MBTA station API and pass information in JSON format
def get_station_response():
    MBTA = []

    with open('MBTA_Distances.csv', mode='r') as CSVfile:
        file = csv.reader(CSVfile)

        for lines in file:
            MBTA.append(lines)

    # return the array
    return MBTA


# helper function to print the MBTA list
def print_array(arr):
    # iterate over the list
    for station in arr:
        # print each station
        print(str(station))


# main function to run the program
if __name__ == '__main__':
    # getting the station & ridership data
    station_data = get_station_response()

    # printing to see output(s)
    print_array(station_data)
