class Tiles:
    def __init__(self, type):
        tiles = {}
        tiles['3'] = {"N": [], "W": ['E'], "E": ['W'], "S": []}
        tiles['5'] = {"N": [], "W": [], "E": ['S'], "S": ['E']}
        tiles['6'] = {"N": [], "W": ['S'], "E": [], "S": ['W']}
        tiles['7'] = {"N": [], "W": ['E', 'S'], "E": ['S', 'W'], "S": ['W', 'E']}
        tiles['9'] = {"N": ['E'], "W": [], "E": ['N'], "S": []}
        tiles['A'] = {"N": ['W'], "W": ['N'], "E": [], "S": []}
        tiles['B'] = {"N": ['W', 'E'], "W": ['E', 'N'], "E": ['W', 'N'], "S": []}
        tiles['C'] = {"N": ['S'], "W": [], "E": [], "S": ['N']}
        tiles['D'] = {"N": ['E', 'S'], "W": [], "E": ['S', 'N'], "S": ['N', 'E']}
        tiles['E'] = {"N": ['S', 'W'], "W": ['S', 'N'], "E": [], "S": ['E', 'N']}
        tiles['F'] = {"N": ['W', 'E', 'S'], "W": ['E', 'S', 'N'], "E": ['N', 'S', 'W'], "S": ['N', 'E', 'W']}
        tiles['96'] = {"N": ['E'], "W": ['S'], "E": ['N'], "S": ['W']}
        tiles['A5'] = {"N": ['W'], "W": ['N'], "E": ['S'], "S": ['E']}
        tiles['C3'] = {"N": ['S'], "W": ['E'], "E": ['W'], "S": ['N']}
        self.type = type
        self.directions = tiles[type]

    def outputs(self, entree):
        return self.directions[entree]