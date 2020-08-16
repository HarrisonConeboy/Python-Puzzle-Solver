from node import Node
from grid import Grid
from shape import Shape
import timeit

class Solver():

    def __init__(self, gridMatrix, shapeMatrices):
        self.nodes = self.setup_node(gridMatrix, shapeMatrices)


    def setup_node(self, gridMatrix, shapeMatrices):
        shapes = [Shape(shape) for shape in shapeMatrices]
        return [Node(Grid(gridMatrix, shapes), 0)]


    def binary_insert(self, node):
        lowerBound = 0
        upperBound = len(self.nodes)-1 if len(self.nodes) > 0 else 0
        mid = int((lowerBound+upperBound)//2)

        while lowerBound != upperBound:
            if node.score > self.nodes[mid].score:
                lowerBound = mid+1
            else:
                upperBound = mid
            mid = int((lowerBound+upperBound)//2)

        if len(self.nodes) == 0:
            self.nodes.append(node)
        else:
            if node.score > self.nodes[mid].score:
                if mid == len(self.nodes)-1:
                    self.nodes.append(node)
                else:
                    self.nodes.insert(mid+1, node)
            else: self.nodes.insert(mid, node)


    def run(self):
        userInput = ''

        start = timeit.default_timer()
        while(len(self.nodes) > 0):
            nodeToExpand = self.nodes.pop(0)
            if not nodeToExpand.grid.can_solve():
                print('great')
                continue
            if nodeToExpand.finished:
                # stop = timeit.default_timer()
                # print(f'It took {stop-start} seconds to find a solution')
                # print('Solution found:')
                # for row in nodeToExpand.grid.mat:
                #     print(row)
                yield nodeToExpand.grid.mat

                # while (userInput != 'y' and userInput != 'n'):
                #     userInput = input('\nWould you like to find another?(y/n)\n').lower()
                # if userInput == 'n': break
                # else:
                #     userInput = ''
                #     start = timeit.default_timer()

            nodesToAdd = nodeToExpand.make_child_nodes()
            for node in nodesToAdd:
                self.binary_insert(node)
        raise StopIteration
        # print('\nNo (more) solutions found, exiting program')














