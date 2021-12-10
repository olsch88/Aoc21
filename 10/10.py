
import numpy as np

with open("10_input.txt", "r") as file:
    data_raw = file.readlines()


openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]

points = {")":3,
        "]": 57,
        "}": 1197,
        ">": 25137
        }

def is_corrupted(s: str) -> bool:
    opend = []
    closed = []
    for d in s:
        if d in openings:
            opend.append(d)
        else: 
            closed.append(d)
            if d != closings[openings.index(opend[-1])]:
                return points[d]
            else:
                opend.pop()
                closed.pop()
    return 0

syntax_error_score = 0
for line in data_raw:
    line = line.strip()
    syntax_error_score += is_corrupted(line)

print("Solution Part 1:")
print(syntax_error_score)

#Part 2
# same funktion as above with slight modifications

points2 = {")":1,
        "]": 2,
        "}": 3,
        ">": 4
        }
def incomplete_score(s: str) -> bool:
    opend = []
    closed = []
    score = 0
    for d in s:
        if d in openings:
            opend.append(d)
        else: 
            closed.append(d)
            if d != closings[openings.index(opend[-1])]:
                pass
                # return points[d]
            else:
                opend.pop()
                closed.pop()
    if len(opend)> len(closed):         
        for c in opend[::-1]:        
            score = score * 5
            score = score + points2[closings[openings.index(c)]]
        return score
    return 0

incomp_score = []
for line in data_raw:
    line = line.strip()
    if is_corrupted(line)>0:
        continue
    incomp_score.append( incomplete_score(line))
incomp_score = np.array(incomp_score)

print("Solution Part 2:")
print(np.median(incomp_score))
