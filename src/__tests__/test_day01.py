import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))
)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from day01.solution import solve


def test_sum_2_combinations():
    """
    Test for combination of 2 (x + y == 2020)
    """
    assert solve([1721, 979, 366, 299, 675, 1456], 2) == 514579


def test_sum_3_combinations():
    """
    Test for combination of 3 (x + y + z == 2020)
    """
    assert solve([1721, 979, 366, 299, 675, 1456], 3) == 241861950
