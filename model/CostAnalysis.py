import matplotlib.pyplot as plt
from scipy.stats import norm


# function to calculate the distance using the flat rate of $2.70
def calculate_cost(distance: float):
    return round((2.70 / distance), 2)


# function to calculate cost of all rides from one starting station
def calculate_all_costs(distances):
    cost_arr = []

    # iterate over all the distances
    for key in distances:
        # discard when source = dest
        if distances[key]['weight'] != 0:
            # calculate the cost per mile and store in array
            cost_arr.append(calculate_cost(distances[key]['weight']))

    # return the final array
    return cost_arr


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


# TODO: trying to make a plot of the costs
# https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# function to plot the array
def plot_the_calc(data):
    mu, std = norm.fit(data)
    plt.hist(data, bins=100, density=True, alpha=0.6, color='blue')
    title = "Fit Values: {:.2f} and {:.2f}".format(mu, std)
    plt.title(title)
    plt.show()


def run_calc(distances, start: str, end: str):
    print("\n## PRICE CALC ##")

    # cost_per_mile calc for the trip
    cost_per_mile = calculate_cost(round(distances[end]["weight"], 2))
    print("Cost per mile: $" + str(cost_per_mile))
    print("Average cost from " + start + ": $" + str(round(calculate_avg_cost(distances), 2)))

    # cost_per_mile for all distances in the array
    plot_the_calc(calculate_all_costs(distances))