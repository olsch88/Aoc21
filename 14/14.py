
from typing import Dict
from collections import Counter

with open("14_input.txt", "r") as f:
#with open("14_sample.txt", "r") as f:
    data = f.readlines()

template = data[0].strip()
print("Template: ")
print(template)
mapping = {line.strip().split(" -> ")[0]:line.strip().split(" -> ")[1] for line in data[2:]}
# print (mapping)
steps = [template,]

def get_insertion(temp: str):
    insert_indices = []
    insert_chars = []

    for key in mapping:
        pos = -1
        while True:
            pos = temp.find(key, pos+1) 
            if pos == -1:
                break
            insert_indices.append(pos)
            insert_chars.append(mapping[key])

    return [insert_indices, insert_chars]

for i in range(11):
    # print(i)
    shift = 0
    next_step = steps[i]
    insert_indices, insert_chars = get_insertion(next_step)
    for i, c in sorted(zip(insert_indices, insert_chars)):
        next_step = next_step[:i+1+shift]+c+next_step[i+1+shift:]
        shift += 1
    steps.append(next_step)
# print(steps)

# sample_step = [steps[0]]
# sample_step.append("NCNBCHB")
# sample_step.append("NBCCNBBBCBHCB")
# sample_step.append("NBBBCNCCNBBNBNBBCHBHHBCHB")
# sample_step.append("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")

# for i in range(5):
#     print(sample_step[i] == steps[i])
# print(len(steps[5])==97)
# print(len(steps[10])==3073)

def count_letters(step: str) -> Dict[str, int]:
    counts = {}    
    for c in set(step):
        counts[c] = step.count(c)
    return counts

c = count_letters(steps[10])
print("Solution Part 1:")
print(c)


######### Part 2 with new Method##########
# We need two counters
# 1 Counts the absolute count for every character
# 2 counts each Letter-Pairs
# For every step a new Counter of Letter-Pairs is generated based on the rules

template = steps[0] # get the starting template from above
pair_counters = [] # A List to store the counters for every step
letter_counter = Counter(template)

start_counter = Counter() # Generate the count of the start pairs
for i in range(len(template)-1):
    start_counter[template[i:i+2]] += 1

pair_counters.append(start_counter)
print(start_counter)
print(letter_counter)

for i in range(40):
    next_pair_counter = Counter() # create a new counter for every step    

    for pair in pair_counters[i]:
        middle = mapping[pair]
        #for j in range(pair_counters[i][pair]):            
        next_pair_counter[pair[0]+middle] += pair_counters[i][pair]
        next_pair_counter[middle+pair[1]] += pair_counters[i][pair]
        letter_counter[middle] += pair_counters[i][pair]

    pair_counters.append(next_pair_counter)
# print(letter_counter.most_common())
# print(letter_counter.most_common()[0])
# print(letter_counter.most_common()[-1])
print("Solution for Part 2:")
print(letter_counter.most_common()[0][1]-letter_counter.most_common()[-1][1])
