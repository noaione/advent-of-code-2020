import typing as t


def remap(cpass: str):
    policy, passwd = cpass.split(": ")
    rangenum, code = policy.split(" ")
    s, e = rangenum.split("-")
    return {
        "code": code,
        "s": int(s),
        "e": int(e),
        "pass": passwd
    }


def solve_a(input_mapped: t.List[dict]) -> int:
    valid = 0
    for data in input_mapped:
        total_char = data["pass"].count(data["code"])
        if total_char >= data["s"] and total_char <= data["e"]:
            valid += 1
    return valid


def solve_b(input_mapped: t.List[dict]) -> int:
    valid = 0
    for data in input_mapped:
        fn_val = data["pass"][data["s"] - 1] == data["code"]
        ln_val = data["pass"][data["e"] - 1] == data["code"]
        if fn_val:
            if not ln_val:
                valid += 1
        elif ln_val:
            if not fn_val:
                valid += 1
    return valid


if __name__ == "__main__":
    in_data = [num.rstrip() for num in open("input", "r").readlines() if num]
    # in_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    mapped_data = [remap(c) for c in in_data]
    print(f"Part A: {solve_a(mapped_data)}")
    print(f"Part B: {solve_b(mapped_data)}")
