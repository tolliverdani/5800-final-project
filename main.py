from model.BuildGraph import *
from model.CompareAlgos import *
from model.ShortestPath import select_station

# main function to run the program
if __name__ == '__main__':
    # build graph by adding nodes & edges
    graph = build_graph()

    # get input values from the user
    start = select_station(graph, "START")
    end = select_station(graph, "END")

    # run the comparison algos
    compare_algos(graph, start, end)
