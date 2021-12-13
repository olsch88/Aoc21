import numpy as np

with open("13_input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

data_coord = [] # Coordinates for the starting points
folds = [] # folding instructions

for line in data: # Parsing the data into the above lists
    if "fold" not in line and line !="":
        data_coord.append(line)
    elif "fold" in line:
        folds.append([line.split("=")[0][-1], int(line.split("=")[1])])

data_coord = [[int(ele.split(",")[0]), int(ele.split(",")[1])] for ele in data_coord]
# getting the maximum dimensions
max_x = max_y = 0
for ele in data_coord:
    if ele[0]>max_x:
        max_x = ele[0]
    if ele[1]>max_y:
        max_y = ele[1]

# setting up the "paper"
grid = np.zeros((max_y+1, max_x+1))

for cord in data_coord:
    grid[cord[1], cord[0]] = 1

def fold(grid, pos: int, axis: str) -> np.ndarray:
    if axis == "y":
        if grid.shape[0]%2 == 0:
            grid[1:pos, :] +=  grid[pos*2+1:pos:-1, :]
            grid_fy = grid[:pos, :]
        else:
            grid_fy =  grid[:pos, :] + grid[pos*2+1:pos:-1, :]        
        return grid_fy        
    if axis == "x":
        if grid.shape[1]%2 == 0:
            grid[:, 1:pos] += grid[:, pos*2+1:pos:-1 ]
            grid_fx = grid[:, :pos]
        else:
            grid_fx =  grid[:, :pos] + grid[:,pos*2:pos:-1]    
        return grid_fx

# Solution part 1:
print("Solution Part 1: ")
print(np.sum(np.where(fold(grid, folds[0][1],folds[0][0] )>0, 1,0)))

# Solution Part 2:
folded_grid = grid.copy()
for f in folds:
    folded_grid = fold(folded_grid, f[1], f[0])
folded_grid = np.where(folded_grid>0, 1, 0)
print("Solution Part 2:")
print(folded_grid)
