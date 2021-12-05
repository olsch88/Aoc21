import numpy as np

with open("04_input.txt", "r") as file:
    data_raw = file.readlines()

numbers_drawn = data_raw[0].strip().split(",")
print(len(numbers_drawn))
numbers_drawn = [int(x) for x in numbers_drawn]
print(len(numbers_drawn))

bingos = []

bingo = []
for i, line in enumerate(data_raw):
    if i == 0:
        continue
    if i == 1:
        continue    
    if not line =="\n":
        bingo.append(line.strip().split())
    else:
        bingos.append(bingo)
        bingo = []

new_bingos = []
for bingo in bingos:
    # print(bingo)
    bingo = np.array([[int(x) for x in line]  for line in bingo])
    # print(bingo)
    new_bingos.append(bingo)
bingos = new_bingos


def check_bingo(bingo: np.array) -> bool:
    for i in range(bingo.shape[0]):
        if np.all(bingo[:,i]==-1):
            print("bingo!")
            print(bingo)
            print(np.sum(np.where(bingo==-1, 0, bingo)))
            return True
    for i in range(bingo.shape[1]):
        if np.all(bingo[i,:]==-1):
            print("bingo!")
            print(bingo)   
            print(np.sum(np.where(bingo==-1, 0, bingo)))
            return True
    return False

new_bingos = []
stop = False
has_won = [False]*len(bingos)
for n in numbers_drawn:
    if stop:
        break
    new_bingos = []
    for i, bingo in enumerate(bingos):

        bingo = np.where(bingo==n, -1, bingo)
        new_bingos.append(bingo)
        if has_won[i]:
            continue

        if check_bingo(bingo):
            print(n)
            has_won[i] = True
            #stop=True
            #break        
    bingos = new_bingos
print(has_won)
print(len(has_won))
#def check_number(bingos: np.array, n: int)-> None:
