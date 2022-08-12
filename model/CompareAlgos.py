from model.CostAnalysis import *
from model.ShortestPath import *


def compare_algos(graph, start: str, end: str):
    # run the distances using nested loops
    distances = shortest_path(graph, start)
    print_path(start, end, distances)

    # run the distances using heap
    distances2 = shortest_path_heap(graph, start)
    print_path(start, end, distances2)

    print("\n## TOTAL DISTANCE ##")
    print(start + " to " + end + " = "
          + str(round(distances[end]["weight"], 2))
          + " miles")

    run_calc(distances, start, end)

