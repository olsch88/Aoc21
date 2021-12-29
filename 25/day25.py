import numpy as np

def read_data(filename):
    with open(filename, "r") as file:
        data_raw = file.readlines()
    convert={".":0,
             ">":1,
             "v":2}
    data = np.array([[convert[c] for c in line.strip() ] for line in data_raw])
    print(data)
    return data

east = np.array([0,1])
south = np.array([1,0])

def step_east(grid: np.ndarray) -> np.ndarray:
    new_grid = grid.copy()
    positions = np.argwhere(grid==1)
    x = [p[1]for p in positions]
    y = [p[0]for p in positions]
    for r,c in zip(y,x):
        try:
            if grid[r,c+1]==0:
                new_grid[r,c+1]=1
                new_grid[r,c]=0
        except IndexError: # Over the edge
            if grid[r,0]==0:
                new_grid[r,0]=1
                new_grid[r,c]=0
    return new_grid
    

def step_south(grid: np.ndarray) -> np.ndarray:
    new_grid = grid.copy()
    positions = np.argwhere(grid==2)
    
    x = [p[1]for p in positions]
    y = [p[0]for p in positions]
    for r,c in zip(y,x):
        
        try:
            if grid[r+1,c]==0:
                # print("move south")
                new_grid[r+1,c]=2
                new_grid[r,c]=0
        except IndexError: # Over the edge
            if grid[0,c]==0:
                new_grid[0,c]=2
                new_grid[r,c]=0
    
    return new_grid
    
def solve_part1(grid: np.ndarray) -> int:
    grid = grid.copy()
    step_count = 0
    while True:
        step_count += 1
        new_grid = step_east(grid)
        new_grid = step_south(new_grid)
        if np.all(new_grid==grid):
            return step_count
        grid = new_grid
        
if __name__ == "__main__":
    start_grid = read_data("25_input.txt")
    sol_part_1 = solve_part1(start_grid)
    print("Soultion Part 1: {}".format(sol_part_1))