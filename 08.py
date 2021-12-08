
from typing import List
import numpy as np

def overlap(s1: str, s2: str) -> int:
    '''returns the number of unique chars in both strings
    '''
    count = 0
    chars_found = []
    for c in s1:
        if c in s2 and c not in chars_found:
            count += 1
            chars_found.append(c)
    for c in s2:
        if c in s1 and c not in chars_found:
            count += 1
            chars_found.append(c)
    return count

# use for testing: Returns 8, 3, 9, 4
# sample = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"

def decode(st: str) -> List[int]:
    '''returns the 4 decoded numbers as a List
    '''
    code = st.split("|")[0].split()
    cipher = st.split("|")[1].strip().split()
    solution = {}
    for element in code: # first, we find the obvious
        element = ''.join(sorted(element)) # for easier comparison
        if len(element) == 2:
            solution[1] = element
        elif len(element) == 3: 
            solution[7] = element
        elif len(element) == 4: 
            solution[4] = element
        elif len(element) == 7: 
            solution[8] = element
    for element in code:
        element = ''.join(sorted(element)) # for easier comparison
        if len(element) == 5:
            if overlap(element, solution[1]) == 2:
                solution[3] = element
            elif overlap(element, solution[4]) == 2:
                solution[2] = element
            else:
                solution[5] = element
        if len(element) == 6:
            if overlap(element, solution[4]) == 4:
                solution[9] = element
            elif overlap(element, solution[7]) == 2:
                solution[6] = element
            else:
                solution[0] = element
    solution = {y:x for x,y in solution.items()}

    result = [solution[''.join(sorted(x))] for x in cipher]

    return result


with open("08_input.txt", "r") as file:
    data = file.readlines()

deciphered = []
for line in data:
    deciphered.append(decode(line))

count = 0
for line in deciphered:
    for num in line:
        if num in  [1,4,7,8]:
            count += 1
print("Solution Part 1:")
print(count)

# Part 2
# converting list of ints into a single int
deciphered_str = [[str(x)for x in line ] for line in deciphered]
deciphered_4_digits = [int("".join(line)) for line in deciphered_str]
print("Solution Part 2:")
print(np.sum(deciphered_4_digits))