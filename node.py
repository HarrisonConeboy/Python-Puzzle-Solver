from grid import Grid
from shape import Shape

class Node():

    def __init__(self, grid, score):
        self.grid = grid
        self.score = score
        self.finished = len(self.grid.shapes) == 0


    def make_child_nodes(self):
        outputNodes = []
        for shape in self.grid.suitablePieces.keys():
            outputNodes.append(Node(self.grid.add_piece(shape), self.calculate_child_score(shape)))
            # print('The shape is:')
            # for row in shape.mat:
            #     print(row)
            # print(f'The score for this shape is: {self.calculate_child_score(shape)}')
            # print('')
        return outputNodes


    def calculate_child_score(self, shape):
        return (1/shape.volume) * (shape.perimeter/(self.calculate_sides_covered(shape)+1)) #+ self.score


    def calculate_sides_covered(self, shape):
        mat = self.grid.mat
        pos = self.grid.insert
        sides_touching = 0

        for i, row in enumerate(shape.mat):
            for j, value in enumerate(row):
                if value == 1:
                    # Check boundaries, this is similar to other methods
                    if pos[0]+i == 0: sides_touching+=1
                    if pos[1]+j == 0: sides_touching+=1
                    if pos[0]+i == len(mat)-1: sides_touching+=1
                    if pos[1]+j == len(mat[0])-1: sides_touching+=1

                    # Check surrounding spaces for non zeros
                    if pos[0]+i > 0 and mat[pos[0]+i-1][pos[1]+j] != 0: sides_touching+=1
                    if pos[1]+j > 0 and mat[pos[0]+i][pos[1]+j-1] != 0: sides_touching+=1
                    if pos[0]+i < len(mat)-1 and mat[pos[0]+i+1][pos[1]+j] != 0: sides_touching+=1
                    if pos[1]+j < len(mat[0])-1 and mat[pos[0]+i][pos[1]+j+1] != 0: sides_touching+=1
        return sides_touching



# s1 = Shape([[1,1], [1,0], [1,0]])
# s3 = Shape([[1]])
# s4 = Shape([[1,1],[1,1]])
# s5 = Shape([[1],[1],[1]])
# s6 = Shape([[0,1,0],[1,1,1],[0,1,0]])
#
# g = Grid([[0,0,0],[0,0,0],[0,0,0]], [s1,s3,s4])#,s4,s5,s6])
#
# n = Node(g, 1)
# print('The grid is:')
# for row in n.grid.mat:
#     print(row)
# print('')
# new_n = n.make_child_nodes()[0].make_child_nodes()[0]
# print(new_n)
# print('')
# print('The grid is:')
# for row in new_n.grid.mat:
#     print(row)
# print('\n\n')
# print(new_n.finished)


