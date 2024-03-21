from Lecteur_v1 import Lecteur_v1
from Point import GoldenPoint, SilverPoint

class Grid():
    
    __slots__ = ["lecteur", "grid", "golden_points", "silver_points"]
    
    def __init__(self, lecteur: Lecteur_v1):
        self.lecteur: Lecteur_v1 = lecteur
        self.grid: list[list[str]] = []
        self.golden_points: list[list[int]] = []
        self.silver_points: list[list[int]] = []
    
    def create_grid(self):
        for i in range(self.lecteur.height):
            self.grid.append(["." for _ in range(self.lecteur.width)])
        
        for i in range(self.lecteur.nb_golden_point):
            x, y = self.lecteur.golden_points[i].get_coords()
            self.golden_points.append([int(x), int(y)])
            self.grid[int(y)][int(x)] = "G"
        
        for i in range(self.lecteur.nb_silver_point):
            x, y = self.lecteur.silver_points[i].get_coords()
            value = self.lecteur.silver_points[i].get_value()
            self.silver_points.append([int(x), int(y), int(value)])
            self.grid[int(y)][int(x)] = "S"
    
    def __str__(self) -> str:
        return str(self.grid)
    
    def display_grid(self):
        for i in range(self.lecteur.height):
            print(" ".join(self.grid[i]))

if __name__ == "__main__":
    lecteur = Lecteur_v1("00-trailer.txt")
    lecteur.process_data()
    print(lecteur)
    grid = Grid(lecteur)
    grid.create_grid()
    grid.display_grid()