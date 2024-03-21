from next_tile import next_tile, next_dir
from Lecteur_v1 import Lecteur_v1
from Tiles import Tile

def next_coord(direction, x, y):
        if direction == "N":
            return x , y + 1
        if direction == "S":
            return x, y - 1
        if direction == "E":
            return x + 1, y
        if direction == "W":
            return x - 1, y
        
def goal_reached(x, y, x_goal, y_goal):
    if abs(x - x_goal) == 1 and abs(y - y_goal) == 0 or abs(x - x_goal) == 0 and abs(y - y_goal) == 1:
        return True
    else:
        return False

def find_path(lecteur: Lecteur_v1, x_start, y_start, x_end, y_end, path = []):
    """
    Fonction qui renvoie le chemin entre deux points
    :param lecteur: Lecteur_v1
    :param x_start: int
    :param y_start: int
    :param x_end: int
    :param y_end: int
    :return: list
    """
    dir = next_dir(x_start, y_start, x_end, y_end)
    nextx, nexty = next_coord(dir, x_start, y_start)
    next_direction = next_dir(nextx, nexty, x_end, y_end)
    next_tiles = next_tile(dir, next_direction, lecteur.costs, lecteur.tiles_av)
    if next_tiles == []:
        print("No path found")
        return path
    else:
        path.append(Tile(next_tiles[0][0], nextx, nexty))
        lecteur.place_tile(Tile(next_tiles[0][0], nextx, nexty))
        if goal_reached(nextx, nexty, x_end, y_end):
            print("got to the end")
            return path
        else:
            
            return find_path(lecteur, nextx, nexty, x_end, y_end, path)
        


lecteur = Lecteur_v1("00-trailer.txt")
lecteur.process_data()
point1 = lecteur.golden_points[0]
point2 = lecteur.golden_points[1]
point3 = lecteur.golden_points[2]
x1,y1 = point1.get_coords()
x2,y2 = point2.get_coords()
x3,y3 = point3.get_coords()
find_path(lecteur, x1, y1, x2, y2)
find_path(lecteur, x2, y2, x3, y3)
lecteur.export()


