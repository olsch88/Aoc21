import numpy as np
from matplotlib import pyplot as plt

# toggle comments to switch beetween sample and input
with open("09_input.txt", "r") as file:
# with open("09_sample.txt", "r") as file:
    data_raw = file.readlines()

data = np.array([[int(x)for x in line.strip()]for line in data_raw])

# create an array that adds a "wall" this will remove edge-cases when looking for the low points
expanded = np.full((data.shape[0]+2, data.shape[1]+2 ),9)

expanded[1:-1, 1:-1] = data

risk_sum = 0
low_points = []
for row in range(1, expanded.shape[0]-1):
    for col in range(1, expanded.shape[1]-1):
        if (expanded[row, col] < expanded[row-1, col] and
         expanded[row, col] < expanded[row+1, col] and
         expanded[row, col] < expanded[row, col-1] and
         expanded[row, col] < expanded[row, col+1] ):
         low_points.append([row, col]) # We need these for Part 2
         risk_sum += expanded[row, col] +1
print(low_points)

print("Solution Part 1: ")
print(risk_sum)

# Par 2
# reduce Map to 1s and 9s
flat = np.where(expanded!=9, 1,9)

# plt.imshow(flat, cmap="RdYlGn")
# plt.show()

def check_point(grid: np.ndarray, row: int, col: int, count: int=0)-> bool:
    if grid[row, col] == 1:
        grid[row, col] =0
        count +=1
        count = check_point(grid, row-1, col, count)
        count = check_point(grid, row+1, col, count)
        count = check_point(grid, row, col-1, count)
        count = check_point(grid, row, col+1, count)
    return count

basin_sizes = []
for point in low_points:
    basin_sizes.append(check_point(flat, point[0],point[1]))

# Sort the list and take the 3 biggest numbers
basin_sizes = sorted(basin_sizes)

print("\nSolution Part 2: ")
print(basin_sizes[-3]*basin_sizes[-2]*basin_sizes[-1])