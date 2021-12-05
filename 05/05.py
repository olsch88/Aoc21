import numpy as np
from dataclasses import dataclass
from typing import List


@dataclass
class Point():
    x: int
    y: int

@dataclass
class Line():
    p1: Point
    p2: Point

    def __init__(self, input_line: str) -> None:
        ''' get the start and endpoint from one line of input
        '''
        p1_str, p2_str = input_line.split("->")
        self.p1 = Point(int(p1_str.split(",")[0]), int(p1_str.split(",")[1]))
        self.p2 = Point(int(p2_str.split(",")[0]), int(p2_str.split(",")[1]))

    def is_straight(self) -> bool:
        '''
        gibt an, ob die Linie senkrecht oder waagerecht ist
        '''
        return (self.p1.x == self.p2.x) or (self.p1.y == self.p2.y)

    def contains(self) -> List[Point]:
        '''
        Gibt eine Liste mit allen Punkten aus, die von der Linie bedeckt werden
        '''
        elements = []
        dir_x = 1 if self.p2.x > self.p1.x else -1 
        dir_y = 1 if self.p2.y > self.p1.y else -1
        
        if not self.is_straight(): # computing diagonal points
            for a, i in enumerate(range(self.p1.y, self.p2.y+dir_y, dir_y)):
                for b, j in enumerate(range(self.p1.x, self.p2.x+dir_x, dir_x)):
                    if a==b:
                        elements.append(Point(j, i))
            return elements
        if (self.p1.x == self.p2.x):
            for i in range(self.p1.y, self.p2.y+dir_y, dir_y):
                elements.append(Point(self.p1.x, i))
            return elements
        if (self.p1.y == self.p2.y):
            for i in range(self.p1.x, self.p2.x+dir_x, dir_x):
                elements.append(Point(i, self.p1.y))
            return elements


### tackling the problems

with open("05_input.txt", "r") as file:
    data_raw = file.readlines()

lines = [Line(line.strip()) for line in data_raw]

# Solving part 1
grid = np.zeros((1000,1000))
# print(grid)
for line in lines:
    if line.is_straight(): # leaving out the diagonals
        for pnt in line.contains():
            grid[pnt.y, pnt.x] +=1
# print(grid)
# counter_grid = np.where(grid>=2, 1,0)
print("Part 1: ")
print(np.sum(np.where(grid>=2, 1,0)))
print("-----------------------\n")



grid = np.zeros((1000,1000))
# print(grid)
for line in lines:
    for pnt in line.contains():
        grid[pnt.y, pnt.x] +=1
# print(grid)
# counter_grid = np.where(grid>=2, 1,0)
print("Part 2: ")
print(np.sum(np.where(grid>=2, 1,0)))
print("-----------------------\n")
