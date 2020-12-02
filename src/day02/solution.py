in_data = [num.rstrip() for num in open("input", "r").readlines() if num]
# in_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


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


# Part A
in_data = [remap(c) for c in in_data]
print(len(in_data))
valid = 0
for data in in_data:
    total_char = data["pass"].count(data["code"])
    if total_char >= data["s"] and total_char <= data["e"]:
        valid += 1
print(f"Part A: {valid}")

valid_b = 0
for data in in_data:
    fn_val = data["pass"][data["s"] - 1] == data["code"]
    ln_val = data["pass"][data["e"] - 1] == data["code"]
    if fn_val:
        if not ln_val:
            valid_b += 1
    elif ln_val:
        if not fn_val:
            valid_b += 1
print(f"Part B: {valid_b}")