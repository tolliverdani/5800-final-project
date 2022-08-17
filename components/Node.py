# node class to store the MBTA station information
class Node:

    # constructor that takes in station name
    def __init__(self, station: str):
        self.station = station
        self.color = []
        # edges will be a tuple ("destination", "color", weight)
        self.edges = []

    def getStation(self):
        return self.station

    def addEdge(self, station: str, color: str, weight: float):
        self.edges.append((station, color, weight))

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
        return str(self.color) \
               + " " + str(self.edges)
