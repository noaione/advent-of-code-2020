import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))
)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from day02.solution import solve_a, solve_b, remap


def test_remapping():
    """
    Test mapping code
    """
    in_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert remap(in_data[0]) == {'code': 'a', 's': 1, 'e': 3, 'pass': 'abcde'}


def test_part_a():
    """
    Test part A solver
    """
    in_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    mapped_data = [remap(c) for c in in_data]
    assert solve_a(mapped_data) == 2


def test_part_b():
    """
    Test part B solver
    """
    in_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    mapped_data = [remap(c) for c in in_data]
    assert solve_b(mapped_data) == 1
