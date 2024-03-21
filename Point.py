class GoldenPoint():

    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y



class SilverPoint():

    __slots__ = ["x", "y", "value"]

    def __init__(self, x, y, value):
        self.x: int = x
        self.y: int = y
        self.value: int = value