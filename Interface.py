import tkinter as tk
from Lecteur_v1 import Lecteur_v1


class Interface(tk.Tk):

    def __init__(self, lecteur):
        tk.Tk.__init__(self)
        self.title("Interface")
        self.lecteur = lecteur
        self.canvas = tk.Canvas(self)
        self.geometry(f"{lecteur.width * 20}x{lecteur.height * 20}")
        self.tiles = []

    def create_grid(self):
        for i in range(self.lecteur.height):
            for j in range(self.lecteur.width):
                id = self.canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="lightgrey")
                self.tiles.append([id, i, j])
        self.canvas.pack()
    

if __name__ == "__main__":
    lecteur = Lecteur_v1("00-trailer.txt")
    lecteur.process_data()
    interface = Interface(lecteur)
    interface.create_grid()
    interface.mainloop()
