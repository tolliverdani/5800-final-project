# node class to store the MBTA station information
class Node:

    # constructor that takes in station name and line color
    def __init__(self, station: str):
        self.station = station
        self.color = ""
        self.edges = {}

    def getStation(self):
        return self.station

    def addEdge(self, station: str, weight: int):
        self.edges[station] = weight

    def addColor(self, color: str):
        self.color = color

    def __getitem__(self):
        return self

    # repr that returns the station name
    def __repr__(self):
        return self.station \
               + ", " + self.color \
               + ", " + str(self.edges)
