import tkinter as tk
from Lecteur_v1 import Lecteur_v1
from Grid import Grid
from Tiles import Tile


class Interface(tk.Tk):

    def __init__(self, lecteur: Lecteur_v1, grid: Grid):
        tk.Tk.__init__(self)
        self.title("Interface")
        self.lecteur = lecteur
        self.grid = grid
        self.canvas = tk.Canvas(self)
        self.geometry(f"{(lecteur.width) * 20}x{(lecteur.height) * 20}")
        self.tiles = dict()

    def create_grid(self):
        for i in range(self.lecteur.height):
            for j in range(self.lecteur.width):
                id = self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="lightgrey")
                self.tiles[id] = [i, j]
        self.canvas.pack()
    
    def fill_grid_with_point(self):

        for i in range(self.lecteur.nb_golden_point):
            x, y = self.lecteur.golden_points[i].get_coords()
            id = self.canvas.find_closest(x * 20 + 10, y * 20 + 10)
            self.canvas.itemconfig(id, fill="yellow")
        
        for i in range(self.lecteur.nb_silver_point):
            x, y = self.lecteur.silver_points[i].get_coords()
            id = self.canvas.find_closest(x * 20 + 10, y * 20 + 10)
            self.canvas.itemconfig(id, fill="grey")

    def fill_grid_with_tile(self):
        for i in range(len(self.lecteur.tiles)):
            tile = self.lecteur.tiles[i]
            x, y = tile.get_coords()
            id = self.canvas.find_closest(x * 20 + 10, y * 20 + 10)
            #dessine
        
    def get_delta(self, direction, x, y):
        if direction == "N":
            return x + 10 , y 
        if direction == "S":
            return x + 10, y + 20
        if direction == "E":
            return x + 20, y + 10
        if direction == "W":
            return x, y + 10

    def dessine_tile(self, id, tile: Tile):
        x, y = tile.get_coords()
        for depart in ["N", "W" , "E", "S"]:
            
            arrivees = tile.outputs(depart)
            for arrivee in arrivees:
                self.canvas.create_line(self.get_delta(depart, x * 20, y * 20), (x * 20 +10, y * 20 + 10), fill="black")
                self.canvas.create_line((x * 20 + 10, y * 20 + 10), self.get_delta(arrivee, x * 20, y * 20), fill="black")     
                
                

if __name__ == "__main__":
    lecteur = Lecteur_v1("00-trailer.txt")
    lecteur.process_data()
    grid = Grid(lecteur)
    interface = Interface(lecteur, grid)
    interface.create_grid()
    interface.fill_grid_with_point()
    interface.dessine_tile(0, Tile("C", 2, 2))

    interface.mainloop()