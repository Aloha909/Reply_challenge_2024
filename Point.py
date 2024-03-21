class GoldenPoint():

    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def get_coords(self):
        return self.x, self.y



class SilverPoint():

    __slots__ = ["x", "y", "value"]

    def __init__(self, x, y, value):
        self.x: int = x
        self.y: int = y
        self.value: int = value
    
    def get_coords(self):
        return self.x, self.y

    def get_value(self):
        return self.value