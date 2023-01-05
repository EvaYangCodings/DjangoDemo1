
lst = [(x, x) for x in range(100)]

# [(0, 0), (1, 1)]

YEARS = list(range(1980, 2031))


class TestClass:
    def add(self, y):
        return y+1

def fn(x: TestClass) -> float:
    """

    """

    x.add