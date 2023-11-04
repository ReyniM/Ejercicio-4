import pytest
import doctest
import math

def distance(x, y, otherx, othery) -> float:
    result = math.sqrt(((x - otherx) ** 2) + ((y - othery) ** 2))
    return result

@pytest.mark.parametrize(
    'x1, y1, x2, y2, expected', [(1, 1, 2, 2, 1.4142135623730951)])

def test_distance(x1, y1, x2, y2, expected):
      assert distance(x1, y1, x2, y2) == expected
      doctest.run_docstring_examples(distance, globals())
