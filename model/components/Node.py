# node class to store the MBTA station information
class Node:

    # constructor that takes in station name and line color
    def __init__(self, station: str):
        self.station = station
        self.color = []
        self.edges = {}

    def getStation(self):
        return self.station

    def addEdge(self, station: str, weight: int):
        self.edges[station] = weight

    def addColor(self, color: str):
        if type(color) == list:
            temp = ''
            for char in color:
                temp += char
            if temp not in self.color:
                self.color.append(temp)
        else:
            if color not in self.color:
                self.color.append(str(color))

    # repr that returns the station name
    def __repr__(self):
        return self.station \
               + ", " + str(self.color) \
               + ", " + str(self.edges)
