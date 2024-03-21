from Point import GoldenPoint, SilverPoint

class Lecteur_v1():

    __slots__ = ["path", "data", "width", "height", "nb_golden_point", "nb_silver_point", "nb_tiles_av", "golden_points", "silver_points", "tiles_av"]

    def __init__(self, path):
        self.path: str = path
    
        with open(self.path, "r") as file:
            trailer = file.readlines()
            self.data: list[list[str]] = []
            for line in trailer:
                self.data.append(line.strip())
            self.data[0] = self.data[0].replace("ï»¿", "")

            for i in range(len(self.data)):
                self.data[i] = self.data[i].split(" ")
        
    def process_data(self):
        temp_data = self.data.copy()
        self.width: int = int(self.data[0][0])
        self.height: int = int(self.data[0][1])
        self.nb_golden_point: int = int(self.data[0][2])
        self.nb_silver_point: int = int(self.data[0][3])
        self.nb_tiles_av: int = int(self.data[0][4])
        temp_data = temp_data[1:]

        for i in range(self.nb_golden_point):
            x, y = temp_data[i]
            self.golden_points = GoldenPoint(int(x), int(y))
        temp_data = temp_data[self.nb_golden_point:]

        for i in range(self.nb_silver_point):
            x, y, value = temp_data[i]
            self.silver_points = SilverPoint(int(x), int(y), int(value))
        temp_data = temp_data[self.nb_silver_point:]
        
