from Tiles import Tile

def complementaire(dir):
    return {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}[dir]

def next_tile(entree: str, sortie: str, costs: dict, available_tiles: dict[str:int]) -> list:
    """
    Fonction qui renvoie une liste des tuiles qui peuvent être utilisées pour avancer dans une certaine direction
    :param entree: direction d'entree dans la tuile
    :param sortie: direction de sortie de la tuile
    :param costs: liste des couts de toutes les tuiles
    :param available_tiles: liste des tuiles disponibles
    :return: liste des tuiles possibles par cout croissant
    """

    working_tiles = []
    for tile_type in available_tiles.keys():
        if available_tiles[tile_type] > 0 :
            if sortie in Tile(tile_type).outputs(complementaire(entree)):
                working_tiles.append((tile_type, costs[tile_type]))
    working_tiles.sort(key=lambda el: el[1])
    return working_tiles


def next_dir(x_start, y_start, x_end, y_end):
    lateral = abs(y_end - y_start) < abs(x_end - x_start)
    if lateral:
        if x_end > x_start :
            return "E"
        elif x_end < x_start :
            return "W"
    else :
        if y_end > y_start :
            return "N"
        elif y_end < y_start :
            return "S"

print(next_tile("E", "E" ,{'3': 6, '5': 2, '6': 2, '7': 8, '9': 2, 'A': 2, 'B': 8, 'C': 6, 'D': 8, 'E': 8, 'F': 15}, {'3': 4, '5': 6, '6': 6, '7': 5, '9': 7, 'A': 7, 'B': 5, 'C': 5, 'D': 5, 'E': 5, 'F': 3}))