from Point import GoldenPoint, SilverPoint
from Tiles import Tile

class Lecteur_v1():

    __slots__ = ["path", "data", "width", "height", "nb_golden_point", "nb_silver_point", "nb_types_av", "golden_points", "silver_points", "tiles_av", "costs", "tiles"]

    def __init__(self, path):
        self.path: str = path

        self.tiles = dict()
    
        with open(self.path, "r") as file:
            trailer = file.readlines()
            self.data: list[list[str]] = []
            for line in trailer:
                self.data.append(line.strip())
            self.data[0] = self.data[0].replace("ï»¿", "")

            for i in range(len(self.data)):
                self.data[i] = self.data[i].split(" ")
    
    def __str__(self) -> str:
        return str(self.data)
        
    def process_data(self):
        temp_data = self.data.copy()
        self.width: int = int(self.data[0][0])
        self.height: int = int(self.data[0][1])
        self.nb_golden_point: int = int(self.data[0][2])
        self.nb_silver_point: int = int(self.data[0][3])
        self.nb_types_av: int = int(self.data[0][4])
        temp_data = temp_data[1:]

        self.golden_points = []
        for i in range(self.nb_golden_point):
            x, y = temp_data[i]
            self.golden_points.append(GoldenPoint(int(x), int(y)))
        
        temp_data = temp_data[self.nb_golden_point:]


        self.silver_points = []
        for i in range(self.nb_silver_point):
            x, y, value = temp_data[i]
            self.silver_points.append(SilverPoint(int(x), int(y), int(value)))

        temp_data = temp_data[self.nb_silver_point:]

        self.costs = []
        self.tiles_av = {}
        for i in range(self.nb_types_av):
            identifier, cost, number_available = temp_data[i]
            self.costs.append(cost)
            self.tiles_av[identifier] = int(number_available)
        
    
    def place_tile(self, tile: Tile):
        if self.tiles_av[tile.type] <= 0:
            raise ValueError("No more tile of this type available")
        else:
            self.tiles[tile.get_coords()] = tile

    def get_tile(self, x, y):
        return self.tiles.get((x, y), Tile("0", x, y))


lecteur = Lecteur_v1("00-trailer.txt")
lecteur.process_data()
lecteur.place_tile(Tile("3", 3, 4))
print(lecteur.get_tile(3, 4).get_coords())