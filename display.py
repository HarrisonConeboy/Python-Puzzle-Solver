from solver import Solver
from shape import Shape
from tkinter import *
import random

class Screen():

    def __init__(self):
        self.root = Tk()
        self.intro = Frame(self.root, bg='white', padx=50, pady=50)
        self.display = Frame(self.root, bg='white', padx=50, pady=50)
        self.inputButtons = dict()


        self.grid = None

        self.setup()


    def setup(self):
        self.root.title('Python Puzzle Solver')
        self.root.geometry('1200x800')

        Label(self.intro, text='Detail the size of your grid:', justify=CENTER).grid(row=0, column=1)
        verticalScale = Scale(self.intro, from_=10, to=1, orient=VERTICAL)
        verticalScale.grid(row=1, column=0)
        horizontalScale = Scale(self.intro, from_=1, to=10, orient=HORIZONTAL)
        horizontalScale.grid(row=1, column=2)

        scaleLabel = Label(self.intro, text='The size of the grid is: 1x1')
        scaleLabel.grid(row=2, column=1)

        Button(self.intro, text='Set Grid', command=lambda : self.set_grid(verticalScale, horizontalScale, scaleLabel)).grid(row=3, column=1)

        inputSpace = Frame(self.intro, padx=20, pady=20)
        for x in range(10):
            for y in range(10):
                self.inputButtons[(x,y)] = Button(inputSpace, bg='black', padx=10, pady=4, command=lambda : self.toggleButton(x,y))
                self.inputButtons[(x,y)].grid(row=x, column=y)

        inputSpace.grid(row=4, column=0)

        self.intro.pack(side=LEFT)


    def toggleButton(self, x,y):
        self.inputButtons[(x,y)]['text'] = 'Good'


    def set_grid(self, vScale, hScale, label):
        label['text'] = f'The size of the grid is: {vScale.get()}x{hScale.get()}'



    def run(self):
        self.root.mainloop()






# gridMat = [[0 for _ in range(10)] for _ in range(10)]
# shapeMat = [[[1 for _ in range(9)]] for _ in range(11)]
#
# solver = Solver(gridMat, shapeMat)
# resultGenerator = solver.run()
#
# result = next(resultGenerator)
#
# # How we are going to make the grid look
# resultFrame = Frame(root, bg='white', padx=20, pady=20)
# colourPalette = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(100)]
# colourPalette[0] = '#FFF'
# for x in range(len(result)):
#     for y in range(len(result[0])):
#         Label(resultFrame, padx=10, pady=3, bg=colourPalette[result[x][y]], borderwidth=2,
#               relief='groove').grid(row=x, column=y)
#
# resultFrame.pack()



s = Screen()
s.run()



























# grid = [[0 for _ in range(6)] for _ in range(7)]
# #shapes = [[[1 for _ in range(2)] for _ in range(2)] for _ in range(100)]
# shapes = [
#     [[1,1],
#      [1,0]],
#     [[1],
#      [1],
#      [1],
#      [1]],
#     [[1,0],
#      [1,0],
#      [1,0],
#      [1,1]],
#     [[0,0,1],
#      [1,1,1]],
#     [[1,1,1,1],
#      [1,1,0,0],
#      [1,1,0,0]],
#     [[1,1],
#      [1,0],
#      [1,0]],
#     [[1],
#      [1]],
#     [[1,1],
#      [1,1]],
#     [[0,1,1],
#      [1,1,1],
#      [1,1,1]]
# ]
#
# s = Solver(grid, shapes)
# s.run()
