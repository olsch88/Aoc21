import numpy as np

with open("07_input.txt", "r") as file:
    data_raw = file.readline()

data = np.array([int(x) for x in data_raw.split(",")])

middle = np.median(data)

fuel = 0
for i in data:
    fuel += np.abs(i-middle)
print("Solution Part 1:")
print(fuel)

def gauss_sum(n: int)-> int:
    return n*(n+1)/2

# data = np.array([16,1,2,0,4,2,7,1,2,14])

min_fuel_cost = 99999999999
optimal_pos = 0
for i in range(int(np.mean(data))-100, int(np.mean(data))+100): # The range is just a guess
    fuel_cost = 0
    for crab in data:
        fuel_cost += gauss_sum(np.abs(crab-i))
    if fuel_cost <= min_fuel_cost:
        min_fuel_cost = fuel_cost
        optimal_pos = i
    if fuel_cost > min_fuel_cost:  # if the cost rises, we passt the spot
        break

print("Solution Part 2:")
print("Optimal Position:")
print(optimal_pos)
print("Total Fuel Cost:")
print(min_fuel_cost)
