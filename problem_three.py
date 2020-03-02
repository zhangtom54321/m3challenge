"""
Problem 3: I like to move it, move it
"""
import numpy as np

#load number of trucks for locations on corridors
arr = np.load("arrays.npy")
trucks_per_location = arr.tolist()

#ENVIRONMENTAL COMPUTATIONS

#define social cost per mile for each diesel truck - from environmental computations
cost_per_mile = 0.27

#define distances between each charging station
distances = [35.5675, 23.0113, 23.7788, 23.4375, 31.2500] #distance is range/8, in miles

#calculate total carbon emissions per distance for each route
environmental_costs = [] #output list

for i in range(len(distances)): #this iterates through each route

    total_cost = 0 #this is the environmental cost for that route

    for stop in trucks_per_location[i]:
        cost = distances[i] * stop * cost_per_mile #cost for that stop
        total_cost += cost

    environmental_costs.append(total_cost)

#ECONOMIC COMPUTATIONS

#charger stop computations

#determine number of charges per stop, is trucks/128
chargers_per_location = arr/128

#take sum of all chargers on each route
charger_costs = [] #output list for economic costs

for i in range(len(chargers_per_location)):
    n = sum(chargers_per_location[i])
    cost = (-500*n) + (0.37*16*n)
    charger_costs.append(cost)

#rest stop computations
rest_stop_costs = [] #rest stop cost is money earned for rest stop - money earned for diesel

#distances between each routes
route_lengths = [543.3, 408, 390.4, 706.2, 381.9]

#list constants from tables
c1 = 1347.516
c2 = 5377.758

for i in range(len(trucks_per_location)):
    #determine rest stop gains
    gains = 0
    for stop in trucks_per_location[i]:
        gain_from_stop = c1 * (stop/624)
        gains += gain_from_stop

    #determine rest stop loss from not selling diesel
    loss = c2 * (route_lengths[i]/27.33)

    rest_stop_cost = gains - loss
    rest_stop_costs.append(rest_stop_cost)

#compute total costs and benefits (negative is cost, positive is benefits)
total_costs = []

for i in range(len(trucks_per_location)):
    cost_route = environmental_costs[i] + charger_costs[i] + rest_stop_costs[i]
    total_costs.append(cost_route)
