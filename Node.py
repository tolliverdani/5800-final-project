# node class to store the MBTA station information
class Node:

    # constructor that takes in station name and line color
    def __init__(self, station: str, color: str):
        self.station = station
        self.color = color

    # repr that returns the station name
    def __repr__(self):
        return self.station + ", " + self.color

