import itertools
import typing as T
from functools import reduce


def solve(input_data: T.List[int], combination_of: int) -> int:
    for subset in itertools.combinations(input_data, combination_of):
        if sum(subset) == 2020:
            return reduce(lambda x, y: x * y, subset)
    return float("NaN")


if __name__ == "__main__":
    in_data = [int(num.rstrip()) for num in open("input", "r").readlines() if num]
    print(f"Part A: {solve(in_data, 2)}")
    print(f"Part B: {solve(in_data, 3)}")
