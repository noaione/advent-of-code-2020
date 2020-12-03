import typing as t


def walkthrough(input_data: t.List[str], xmove: int, ymove: int) -> int:
    currx = curry = trees = 0
    while curry < len(input_data):
        if input_data[curry][currx % len(input_data[0])] == "#":
            trees += 1
        currx += xmove
        curry += ymove
    return trees


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]
    print(len(in_data[0]))
    r3d1 = walkthrough(in_data, 3, 1)
    r1d1 = walkthrough(in_data, 1, 1)
    r5d1 = walkthrough(in_data, 5, 1)
    r7d1 = walkthrough(in_data, 7, 1)
    r1d2 = walkthrough(in_data, 1, 2)
    print(f"Part A: {r3d1}")
    print(f"Part B: {r3d1 * r1d1 * r5d1 * r7d1 * r1d2}")
