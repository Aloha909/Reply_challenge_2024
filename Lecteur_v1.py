class Lecteur_v1():

    __slots__ = ["path", "data"]

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
