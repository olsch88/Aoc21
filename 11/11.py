import numpy as np
import time

with open("11_input.txt", "r") as file:
    data_raw = file.readlines()


data = np.array([[int (c) for c in line.strip()]for line in data_raw])
print(data)

dirs = [np.array([-1,-1]),
    np.array([0,-1]),
    np.array([1,-1]),
    np.array([-1,0]),
    np.array([-1, 1]),
    np.array([1,1]), 
    np.array([1,0]),
    np.array([0,1])]

has_flashed = np.full(data.shape, False)
flash_count = 0

def flash(grid, r, c, has_flashed,flash_count):    
    flash_count += 1
    grid[r,c] = 0
    has_flashed[r,c]= True
    for pos in dirs:
        if 0 <= pos[0]+r <10 and 0 <= pos[1]+c <10: # avoiding the edges and overflows
            grid[pos[0]+r, pos[1]+c] += 1
    return flash_count

def scan_flash(grid: np.ndarray, has_flashed, flash_count=0):
    # I think, that there is an easier way to do this with numpy
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] >= 10:
                flash_count = flash(grid,r,c, has_flashed, flash_count)
                # sns.heatmap(grid)
    return flash_count

grid = data
count = 0
def solve(grid: np.ndarray, stop=0):
    count = 0
    flash_count = 0
    while True:
        count += 1
        has_flashed = np.full(grid.shape, False)
        grid = grid + 1
        while(np.any(grid>=10)):
            flash_count = scan_flash(grid, has_flashed, flash_count)
        if np.all(has_flashed):
            print("Solution Part 2:")
            print("Step: {}".format(count))
            break
        grid = np.where(has_flashed, 0, grid)
        has_flashed = np.full(grid.shape, False)
        if count == 100:
            print("Solution Part 1:\n{}".format(flash_count))
        if count == stop:
            break


if __name__ == "__main__":
    start_time = time.perf_counter()
    solve(data)
    print(f"Time to solve Puzzle 11:\n{time.perf_counter()-start_time}")
    
    # Scaling test
    start_time = time.perf_counter()
    data_20 = np.random.randint(0, 10, (20,20))
    solve(data_20, 100)
    print(f"Time to solve 100 iterations of 20x20 Matrix:\n{time.perf_counter()-start_time}")
    
    start_time = time.perf_counter()
    data_100 = np.random.randint(0, 10, (100,100))
    solve(data_100, 100)
    print(f"Time to solve Puzzle 100 iterations of 100x100 Matrix:\n{time.perf_counter()-start_time}")
    