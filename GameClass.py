class Base():
    def __init__(self):
        self.s = 1

class Spot:
    def __init__(self, s1, s2, s3, s4, s=0):
        self.s = s
        self.b = [s1, s2, s3, s4]

    def available(self):
        if self.s: return True
        for s in self.b:
            if not s.s:
                return False
        return True

    def clear(self):
        self.s = 0


class Pylos:
    def __init__(self):
        self.grid = [[[Spot(Base(), Base(), Base(), Base()) for i in range(4)] for i in range(4)]]
        self.pcount = [15, 15]
        for i in range(4, 0, -1):
            nl = [[Spot(self.grid[-1][j][k], self.grid[-1][j][k+1],self.grid[-1][j+1][k], self.grid[-1][j+1][k+1]) for k in range(i)] for j in range(i)]
            self.grid.insert(0, nl)

    def play(self, pos, p):
        spot = self.grid[pos[0]][pos[1]][pos[2]]
        if spot.available() and self.pcount[int(0.5 * p + 0.5)]:
            spot.s = p

    def check(self, pos):
        for dx, dy in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
            if 0 <= pos[1] + dx <= pos[0] and 0 <= pos[2] + dy <= pos[0]:

