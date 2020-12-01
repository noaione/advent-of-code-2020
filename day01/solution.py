# Part A
import itertools

in_data = [int(num.rstrip()) for num in open("input", "r").readlines() if num]
combi = []

for subset in itertools.combinations(in_data, 2):
    if sum(subset) == 2020:
        combi = subset
        break

if combi:
    print(f"Part A: {combi[0] * combi[1]}")

# Part B
combi = []
for subset in itertools.combinations(in_data, 3):
    if sum(subset) == 2020:
        combi = subset
        break

if combi:
    print(f"Part B: {combi[0] * combi[1] * combi[2]}")
