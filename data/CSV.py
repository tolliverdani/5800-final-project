import csv


# TODO: I think this isn't as useful as the API because it iterates
#  over the entire line and their destinations instead of being
#  station to station figures. LMK.


# function to call MBTA station API and pass information in JSON format
def get_bus_data(bus_csv):
    data = {}

    with open(bus_csv, encoding='utf-8') as CSVfile:
        file = csv.DictReader(CSVfile)

        for rows in file:
            key = rows['ObjectId']
            data[key] = rows

    # return the array
    return data


# main function to run the program
if __name__ == '__main__':
    # getting the station & ridership data
    station_data = get_bus_data()

    # printing to see output(s)
    print(station_data)
