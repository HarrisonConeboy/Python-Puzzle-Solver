from shape import Shape

class Grid():

    # We must initialize the grid with the matrix representing empty and occupied spaces, the counter to represent
    # new additions to the grid, a list of shapes provided and an insertion point
    def __init__(self, mat, shapes, counter=1, volume=0, insert=(0,0)):
        self.mat = mat
        self.counter = counter
        self.shapes = [shape.produce_symmetries() if type(shape)==Shape else shape for shape in shapes]
        self.volume = volume if volume else len(mat)*len(mat[0])
        self.suitablePieces = dict()
        self.calc_insert(insert)


    def calc_shapes(self, shapes):
        if type(shapes[0]) == Shape:
            index = 0
            shapesSeen = dict()
            outputShapes = []
            for shape in shapes:
                pass
        else:
            self.shapes = shapes



    # Iterative floodfill algorithm for finding the amount of empty space given a position in the grid
    # This method is not complete as if the first square and its neighbours are full then the algorithm will stop
    def calc_empty_space(self, pos):
        dupes = {pos:True}
        stack = [pos]
        counter = 0 if self.mat[pos[0]][pos[1]] == 0 else -1
        while len(stack) > 0:
            tempPos = stack.pop()
            counter += 1

            # Check down
            if (tempPos[0]+1, tempPos[1]) not in dupes and tempPos[0]+1 < len(self.mat) \
                    and self.mat[tempPos[0]+1][tempPos[1]] == 0:
                stack.append((tempPos[0]+1, tempPos[1]))
                dupes[(tempPos[0]+1, tempPos[1])] = True

            # Check up
            if (tempPos[0]-1, tempPos[1]) not in dupes and tempPos[0]-1 >= 0 \
                    and self.mat[tempPos[0]-1][tempPos[1]] == 0:
                stack.append((tempPos[0]-1, tempPos[1]))
                dupes[(tempPos[0]-1, tempPos[1])] = True

            # Check to the right
            if (tempPos[0], tempPos[1]+1) not in dupes and tempPos[1]+1 < len(self.mat[0]) \
                    and self.mat[tempPos[0]][tempPos[1]+1] == 0:
                stack.append((tempPos[0], tempPos[1]+1))
                dupes[(tempPos[0], tempPos[1]+1)] = True

            # Check to the left
            if (tempPos[0], tempPos[1]-1) not in dupes and tempPos[1]-1 >= 0 \
                    and self.mat[tempPos[0]][tempPos[1]-1] == 0:
                stack.append((tempPos[0], tempPos[1]-1))
                dupes[(tempPos[0], tempPos[1]-1)] = True

        return counter


    # This method will produce a list of shapes which fit in the remaining space determined by pos in the grid
    def calc_suitable(self, pos):
        # self.emptySpace = self.calc_empty_space(pos)
        outputShapes = dict()
        for k, shapeSet in enumerate(self.shapes):
            for shape in shapeSet:
                #if shape.volume <= self.emptySpace and
                if shape.xLength <= len(self.mat[0][pos[1]:])\
                        and shape.yLength <= len(self.mat[pos[0]:]):
                    shapeFits = True
                    for i, row in enumerate(shape.mat):
                        for j, col in enumerate(row):
                            if self.mat[pos[0]+i][pos[1]+j] != 0 and col == 1:
                                shapeFits = False
                    if shapeFits: outputShapes[shape] = k
        return outputShapes


    # This method changes the position of our insertion depending on whether there are suitable pieces to be placed
    # If there are no suitable pieces in our list that fill fit in the current insert value, then the value is increased
    # until an appropriate value is found and suitable pieces, empty space and the insert index are updated
    # This method returns false if no more pieces can fit
    def calc_insert(self, insert):
        for col in range(insert[1], len(self.mat[0])):
            tempSuitable = self.calc_suitable((insert[0], col))
            if len(tempSuitable.keys()) > 0:
                self.suitablePieces = tempSuitable
                self.insert = (insert[0], col)
                return True

        for row in range(insert[0] + 1, len(self.mat)):
            for col in range(len(self.mat[0])):
                tempSuitable = self.calc_suitable((row, col))
                if len(tempSuitable.keys()) > 0:
                    self.suitablePieces = tempSuitable
                    self.insert = (row, col)
                    return True
        self.insert = False
        return False # If no pieces fit



    def add_piece(self, shape, inPlace=False):
        if shape in self.suitablePieces:
            if inPlace:
                for i, row in enumerate(shape.mat):
                    for j, value in enumerate(row):
                        self.mat[self.insert[0]+i][self.insert[1]+j] = self.counter if value == 1 else \
                            self.mat[self.insert[0]+i][self.insert[1]+j]
                del self.shapes[self.suitablePieces[shape]]
                self.calc_insert(self.insert)
                self.counter += 1

            else:
                new_mat = [row[:] for row in self.mat]
                shapes = list(self.shapes)
                newVolume = self.volume-shape.volume
                del shapes[self.suitablePieces[shape]]
                counter = self.counter + 1
                for i, row in enumerate(shape.mat):
                    for j, value in enumerate(row):
                        new_mat[self.insert[0]+i][self.insert[1]+j] = self.counter if value == 1 else \
                            new_mat[self.insert[0]+i][self.insert[1]+j]
                new_grid = Grid(new_mat, shapes, counter, newVolume, self.insert)
                return new_grid
        else:
            print('Shape not suitable to add')


    def can_solve(self):
        return self.volume >= sum([shape[0].volume for shape in self.shapes])



# s1 = Shape([[1,1], [1,0], [1,0]])
# s2 = Shape(s1.rotate_90(s1.rotate_90()))
# s3 = Shape([[1]])
#
# r1 = s1.produce_symmetries()
# r2 = s2.produce_symmetries()
# r3 = s3.produce_symmetries()
#
# g = Grid([[0,0,0],[0,0,0],[0,0,0]], [s1, s2, s3])
# print(len(g.suitablePieces))
#
# print('Before adding:')
# for row in g.mat:
#     print(row)
#
# print('\nAfter adding first piece:')
# g.add_piece(s1, inPlace=True)
# for row in g.mat:
#     print(row)
#
#
# print('\nAfter adding second piece:')
# g.add_piece(s2, inPlace=True)
# for row in g.mat:
#     print(row)
#
# print('\nAfter adding third piece:')
# g.add_piece(s3, inPlace=True)
# for row in g.mat:
#     print(row)





