import typing as T
from functools import reduce
from itertools import combinations


def solve(input_data: T.List[int], combination_of: int) -> int:
    final = filter(lambda subset: sum(subset) == 2020, combinations(input_data, combination_of)).__next__()
    return reduce(lambda x, y: x * y, final)


if __name__ == "__main__":
    in_data = [int(num.rstrip()) for num in open("input", "r").readlines() if num]
    print(f"Part A: {solve(in_data, 2)}")
    print(f"Part B: {solve(in_data, 3)}")
