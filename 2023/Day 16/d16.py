# Advent of Code 2023 - Day 16
# Eetu Knutars / @knuutti

class Beam():
    def __init__(self, loc, dir):
        self.y = loc[0]
        self.x = loc[1]
        self.dir = dir

def main():
    fname = "./2023/Day 16/input.txt"
    file = open(fname, 'r')
    grid = file.read().splitlines()

    R = len(grid)
    C = len(grid[0])

    start_beams = []
    for r in range(R):
        start_beams.append(Beam([r,-1], 'e'))
        start_beams.append(Beam([r,C], 'w'))
    for c in range(C):
        start_beams.append(Beam([-1,c], 's'))
        start_beams.append(Beam([R,c], 'w'))

    max_energy = 0
    for beam in start_beams:
        energy = len(interact(beam, grid, {}))
        if not max_energy:    
            print("Part 1:", energy)
        if energy > max_energy:
            max_energy = energy

    print("Part 2:", max_energy)


def interact(beam: Beam, grid: list, tiles: dict):
    while True:
        # Determine location
        loc = [beam.y, beam.x]
        hor, ver = False, False
        if beam.dir == 'e':
            loc[1] += 1
            ver = True
        elif beam.dir == 'w':
            loc[1] -= 1
            ver = True
        elif beam.dir == 'n':
            loc[0] -= 1
            hor = True
        else: 
            loc[0] += 1
            hor = True

        # Check if outside grid
        if loc[0] < 0 or loc[0] >= len(grid[0]) or loc[1] < 0 or loc[1] >= len(grid):
            return tiles
        # Update the activated tiles
        key = str(loc[0]) + "," + str(loc[1])
        if key not in tiles:
            tiles[key] = [beam.dir]
        elif beam.dir not in tiles[key]:
            tiles[key].append(beam.dir)
        else: # Already been on a tile with given direction
            return tiles

        # Defining the next destination for the beam
        containts = grid[loc[0]][loc[1]]
        if containts == "." or (ver and containts == "-") or (hor and containts == "|"):
            beam = Beam(loc, beam.dir)
        elif containts == "/":
            if beam.dir == 'w': beam = Beam(loc, 's')
            elif beam.dir == 'e': beam = Beam(loc, 'n')
            elif beam.dir == 'n': beam = Beam(loc, 'e')
            else: tiles= interact(Beam(loc, 'w'), grid, tiles)
        elif containts == "\\":
            if beam.dir == 'w': beam = Beam(loc, 'n')
            elif beam.dir == 'e': beam = Beam(loc, 's')
            elif beam.dir == 'n': beam = Beam(loc, 'w')
            else: beam = Beam(loc, 'e')
        elif containts == "-":
            tiles = interact(Beam(loc, 'w'), grid, tiles)
            tiles = interact(Beam(loc, 'e'), grid, tiles)
            break
        else:
            tiles = interact(Beam(loc, 'n'), grid, tiles)
            tiles = interact(Beam(loc, 's'), grid, tiles)
            break

    return tiles






    

if __name__ == '__main__':
    main()