from typing import List

with open("06_input.txt", "r") as source:
    input = source.readline()

start_sample = [3, 4, 3, 1, 2]  # this is  a comment
# this is just another line


def create_counter_list(init_list: List[int]) -> List[int]:
    counter_list = [0]*9
    for i in init_list:
        counter_list[i] += 1
    return counter_list


def process_counter_list(current_day: List[int]) -> List[int]:
    next_day = [0]*9
    for index, count in enumerate(current_day):
        if index == 0:
            next_day[8] += count
            next_day[6] += count
        else:
            next_day[index-1] += count
    return next_day


fish_list = [int(x) for x in input.split(",")]
fish_counter_list = create_counter_list(fish_list)

# Part 1:
for i in range(80):
    fish_counter_list = process_counter_list(fish_counter_list)
print("Solution Part 1:\n{}\n".format(sum(fish_counter_list)))

# Part 2:
# reset list
fish_counter_list = create_counter_list(fish_list)
for i in range(256):
    fish_counter_list = process_counter_list(fish_counter_list)
print("Solution Part 2:\n{}\n".format(sum(fish_counter_list)))
