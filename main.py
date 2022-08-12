from model.BuildGraph import *
from model.CompareAlgos import *
from model.ShortestPath import select_station

# main function to run the program
if __name__ == '__main__':
    # build graph by adding nodes & edges
    graph = BuildGraph()

    # get input values from the user
    START = select_station(graph, "START")
    END = select_station(graph, "END")

    # run the comparison algos
    compareAlgos(graph, START, END)
