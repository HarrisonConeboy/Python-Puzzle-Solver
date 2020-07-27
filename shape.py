class Shape():

    def __init__(self, mat):
        self.mat = mat
        self.volume = self.calc_vol()
        self.symmetry = self.calc_symmetry()
        self.perimeter = self.calc_perimeter()
        self.yLength = len(mat)
        self.xLength = len(mat[0])


    # ROTATIONS and SYMMETRY of the shape given
    ###################################################################
    ###################################################################
    def rotate_90(self, mat=None):
        return self.rotate_90_task(mat or self.mat)


    def rotate_90_task(self, mat):
        newMat = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]
        for x in range(len(mat[0])):
            for i, y in enumerate(range(len(mat))[::-1]):
                newMat[x][i] = mat[y][x]
        return newMat


    def calc_symmetry(self):
        rotate1 = self.rotate_90(self.mat)
        if rotate1 == self.mat: return 2
        elif self.rotate_90(rotate1) == self.mat: return 1
        else: return 0


    def produce_symmetries(self):
        outputShapes = [self]
        if self.symmetry == 1: outputShapes.append(Shape(self.rotate_90()))
        elif self.symmetry == 0:
            outputShapes.append(Shape(self.rotate_90()))
            outputShapes.append(Shape(self.rotate_90(self.rotate_90())))
            outputShapes.append(Shape(self.rotate_90(self.rotate_90(self.rotate_90()))))
        return outputShapes


    # PERIMETER and VOLUME of the shape given
    ###################################################################
    ###################################################################
    def calc_perimeter(self):
        perimeter = 0
        for i, row in enumerate(self.mat):
            for j, value in enumerate(row):
                if value == 1:
                    # Give perimeter for each boundary we encounter if piece present
                    # Top boundary
                    if i == 0: perimeter += 1
                    # Left boundary
                    if j == 0: perimeter += 1
                    # Bottom boundary
                    if i == len(self.mat)-1: perimeter += 1
                    # Right boundary
                    if j == len(self.mat[0])-1: perimeter += 1

                    # Now check surroundings for 0's to determine further perimeter
                    # Check top space
                    if i > 0 and self.mat[i-1][j] == 0: perimeter += 1
                    # Check left space
                    if j > 0 and self.mat[i][j-1] == 0: perimeter += 1
                    # Check bottom space
                    if i < len(self.mat)-1 and self.mat[i+1][j] == 0: perimeter += 1
                    # Check right space
                    if j < len(self.mat[0])-1 and self.mat[i][j+1] == 0: perimeter += 1
        return perimeter


    def calc_vol(self):
        volume = 0
        for x in self.mat:
            for y in x:
                if y == 1: volume += 1
        return volume
