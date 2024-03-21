import tkinter as tk
from Lecteur_v1 import Lecteur_v1
from Grid import Grid


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
            print(i)
            x, y = self.lecteur.golden_points[i].get_coords()
            id = self.canvas.find_closest(x * 20 + 10, y * 20 + 10)
            self.canvas.itemconfig(id, fill="yellow")
        
        for i in range(self.lecteur.nb_silver_point):
            x, y = self.lecteur.silver_points[i].get_coords()
            id = self.canvas.find_closest(x * 20 + 10, y * 20 + 10)
            self.canvas.itemconfig(id, fill="grey")

if __name__ == "__main__":
    lecteur = Lecteur_v1("00-trailer.txt")
    lecteur.process_data()
    grid = Grid(lecteur)
    interface = Interface(lecteur, grid)
    interface.create_grid()
    interface.fill_grid_with_point()
    interface.mainloop()