import matplotlib.pyplot as plt


# function to calculate the distance using the flat rate of $2.70
def calculateCost(distance: float):
    return round((2.70 / distance), 2)


# function to calculate cost of all rides from one starting station
def calculateAllCosts(distances):
    cost_arr = []

    # iterate over all the distances
    for key in distances:
        # discard when source = dest
        if distances[key]['weight'] != 0:
            # calculate the cost per mile and store in array
            cost_arr.append(calculateCost(distances[key]['weight']))

    # return the final array
    return cost_arr


# function to calculate avg cost of all rides from one starting station
def calculateAvgCost(distances):
    total = 0
    count = 0

    # iterate over all the distances
    for key in distances:
        # discard when source = dest
        if distances[key]['weight'] != 0:
            # calculate the cost per mile and store in array
            total += calculateCost(distances[key]['weight'])
            count += 1

    # return the final array
    return total / count


# function to plot the array
def plotCalc(array):
    plt.plot(array)
    plt.title('test')
    plt.show()
