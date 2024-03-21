class Tiles:
    def __init__(self, type):
        tiles = {}
        self.type = type
        self.directions = tiles[type]

    def outputs(self, entree):
        return self.directions[entree]