# function to calculate the distance using the flat rate of $2.70
def calculate_cost(distance: float):
    return round((2.70 / distance), 2)


# function to calculate avg cost of all rides from one starting station
def calculate_avg_cost(distances):
    total = 0
    count = 0

    # iterate over all the distances
    for key in distances:
        # discard when source = dest
        if distances[key]['weight'] != 0:
            # calculate the cost per mile and store in array
            total += calculate_cost(distances[key]['weight'])
            count += 1

    # return the final array
    return total / count


# function that runs the cost analysis on the graph
# and outputs a user-friendly text with the specs
def run_calc(distances, start: str, end: str):
    print("\n## PRICE CALC ##")

    # cost_per_mile calc for the trip
    cost_per_mile = calculate_cost(round(distances[end]["weight"], 2))
    print("Cost per mile for MBTA break even: $" + str(cost_per_mile))
    print("Average cost of all possible routes from " + start + ": $" + str(round(calculate_avg_cost(distances), 2)))