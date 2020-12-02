import configparser
import os
import sys
from datetime import datetime, timezone, timedelta

import requests

config = configparser.ConfigParser()
config.read("aoc.ini")

secret_cookies = config["AoC"]["SESSION_COOKIES"]

session = requests.Session()
session.headers.update({
    "Cookie": f"session={secret_cookies}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",  # noqa: E501
})

wib_tz = timezone(timedelta(hours=7))
current_time = datetime.now(tz=wib_tz)
print(f"[AoC-2020] Current Time: {current_time.strftime('%d %b %Y %H:%M:%S')}")

# AOC New Day started at 12:00PM my time
if current_time.hour >= 12:
    current_day = current_time.day
else:
    current_day = current_time.day - 1

dayf = str(current_day).zfill(2)

if os.path.isdir(f"./src/day{dayf}"):
    print(f"[AoC-2020-Day{dayf}] Day already initialized.")
    sys.exit(0)

wait_for = input(f"[AoC-2020-Day{dayf}] This will prepare day {dayf}, type `c` to cancel")
if wait_for.lower().strip() == "c":
    sys.exit(1)

PYTHON_INIT = """import typing as t

in_data = [num.rstrip() for num in open("input", "r").readlines() if num]

# Part A
print(f"Part A: ")

# Part B
print(f"Part B: ")

if __name__ == "__main__":
    pass
    # in_data = [int(num.rstrip()) for num in open("input", "r").readlines() if num]
    # print(f"Part A: {solve(in_data, 2)}")
    # print(f"Part B: {solve(in_data, 3)}")
"""

JS_INIT = """const utils = require("../utils/utils");

let in_data = utils.readInput("input", true);

// Part A
console.log(`Part A: `)

// Part B
console.log(`Part B: `)
"""

PYTEST_INIT = """import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))
)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from day{}.solution import solve
"""

print(f"[AoC-2020-Day{dayf}] Downloading Input...")
req_input = session.get(f"https://adventofcode.com/2020/day/{current_day}/input")
with open(f"src/day{dayf}/input", "w", encoding="utf-8") as fp:
    fp.write(req_input.text)

print(f"[AoC-2020-Day{dayf}] Generating solution template...")
with open(f"src/day{dayf}/solution.py", "w", encoding="utf-8") as fp:
    fp.write(PYTHON_INIT)
with open(f"src/day{dayf}/solution.js", "w", encoding="utf-8") as fp:
    fp.write(JS_INIT)

print(f"[AoC-2020-Day{dayf}] Generating tests file...")
with open(f"src/__tests__/test_day{dayf}.py", "w", encoding="utf-8") as fp:
    fp.write(PYTEST_INIT.format(dayf))
