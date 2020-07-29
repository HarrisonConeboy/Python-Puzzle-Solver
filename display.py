from solver import Solver
from shape import Shape
from tkinter import *
import random

class Screen():

    def __init__(self):
        # The root tk which contains everything
        self.root = Tk()

        # Variables to keep track of user input shapes
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.inputButtons = dict()
        self.shapes = []

        # Variable for the grid size which contains the pieces
        self.grid_size = [10, 10]
        self.solution = None
        self.shapeDisplay = None
        self.noSolutions = None

        # Initialize the colour palette
        self.colourPalette = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(100)]
        self.colourPalette[0] = '#FFF'

        self.setup()


    def setup(self):
        self.root.title('Python Puzzle Solver')
        self.root.geometry('800x800')

        # self.display_grid_input()
        self.display_shape_input()
        self.display_board_input()


    def display_grid_input(self):
        intro = Frame(self.root)

        Label(intro, text='Detail the size of your grid:', justify=CENTER).grid(row=0, column=1)
        verticalScale = Scale(intro, from_=20, to=5, orient=VERTICAL)
        verticalScale.set(10)
        verticalScale.grid(row=1, column=0)
        horizontalScale = Scale(intro, from_=5, to=20, orient=HORIZONTAL)
        horizontalScale.set(10)
        horizontalScale.grid(row=1, column=2)

        scaleLabel = Label(intro, text='The size of the grid is: 10x10')
        scaleLabel.grid(row=2, column=1)

        Button(intro, text='Set Grid', command=lambda: self.set_grid(verticalScale, horizontalScale, scaleLabel)) \
            .grid(row=3, column=1)

        intro.pack(side=LEFT)


    def display_board_input(self):
        gridInput = Frame(self.root, padx=100, pady=50, borderwidth=2, relief='groove')

        gridDisplay = Frame(gridInput, borderwidth=2, relief='groove')
        Label(gridDisplay, text='Grid Size: ').grid(row=0, column=0)

        self.verticalValue = Label(gridDisplay, text='10x')
        self.verticalValue.grid(row=0, column=1)

        self.horizontalValue = Label(gridDisplay, text='10', justify=LEFT, anchor=W)
        self.horizontalValue.grid(row=0, column=2)

        gridDisplay.grid(row=0, column=0, columnspan=2)

        verticalScale = Scale(gridInput, from_=20, to=3, orient=VERTICAL,
                              command=self.change_vertical)
        verticalScale.set(10)
        verticalScale.grid(row=1, column=0)

        horizontalScale = Scale(gridInput, from_=3, to=20, orient=HORIZONTAL,
                                command=self.change_horizontal)
        horizontalScale.grid(row=1, column=1)
        horizontalScale.set(10)

        gridInput.grid(row=0, column=0)


    def change_vertical(self, value):
        self.verticalValue['text'] = f'{value}x'
        self.grid_size[0] = int(value)


    def change_horizontal(self, value):
        self.horizontalValue['text'] = value
        self.grid_size[1] = int(value)


    def display_shape_input(self):
        shapeInput = Frame(self.root, padx=50, pady=50, borderwidth=2, relief='groove')
        buttonFrame = Frame(shapeInput, padx=20, pady=15)
        for x in range(5):
            for y in range(5):
                tempButton = Button(buttonFrame, padx=10, pady=3, bg='white',
                                    command=lambda x=x, y=y: self.toggle_button(x, y))
                tempButton.grid(row=x, column=y)
                self.inputButtons[(x, y)] = [False, tempButton]

        buttonFrame.grid(row=0, column=1, columnspan=5, rowspan=5)
        Button(shapeInput, text='Reset', pady=3, padx=6, command=self.clear_all).grid(row=4, column=0)
        Button(shapeInput, text='Next', pady=3, padx=6, command=self.clear_and_add).grid(row=4, column=6)
        Button(shapeInput, text='Solve', pady=3, padx=6, command=self.display_solution).grid(row=5, column=6)

        # Feedback section
        shapeFeedback = Frame(shapeInput, borderwidth=2, relief='groove')
        Label(shapeFeedback, text='Number of shapes: ').grid(row=0, column=0)
        self.shapeCount = Label(shapeFeedback, text='0')
        self.shapeCount.grid(row=0, column=1)
        shapeFeedback.grid(row=5, column=0, columnspan=6)

        shapeInput.grid(row=0, column=1)


    def display_solution(self):
        if self.solution:
            self.solution.pack_forget()
            self.solution.destroy()
        elif self.noSolutions:
            self.noSolutions.grid_forget()
            self.noSolutions.destroy()
        solution = Frame(self.root, padx=20)

        solver = Solver([[0 for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])], self.shapes).run()
        try:
            gridSolution = next(solver)
            for x in range(len(gridSolution)):
                for y in range(len(gridSolution[0])):
                    Label(solution, padx=10, pady=3, bg=self.colourPalette[gridSolution[x][y]], borderwidth=2,
                                   relief='groove').grid(row=x, column=y)

            self.solution = solution
            solution.grid(row=1, column=0, columnspan=2)

        except StopIteration as e:
            if self.noSolutions:
                self.noSolutions.grid_forget()
                self.noSolutions.destroy

            self.noSolutions = Label(self.root, text='No (more) solutions to show')
            self.noSolutions.grid(row=1, column=0, columnspan=2)



    def set_grid(self, vScale, hScale, label):
        label['text'] = f'{vScale.get()}x{hScale.get()}'
        self.grid_size[0] = vScale.get()
        self.grid_size[1] = hScale.get()


    def toggle_button(self, x, y):
        tempButton = self.inputButtons[(x, y)]
        if not tempButton[0]:
            tempButton[1].config(background='green')
            self.grid[x][y] = 1
            tempButton[0] = not tempButton[0]
        else:
            tempButton[1].config(background='white')
            self.grid[x][y] = 0
            tempButton[0] = not tempButton[0]


    def clear_all(self):
        for tup in self.inputButtons.keys():
            self.inputButtons[tup][1].config(background='white')
            self.inputButtons[tup][0] = False
            self.grid[tup[0]][tup[1]] = 0
        self.shapes = []
        self.updateCount()


    def clear_and_add(self):
        if self.determine_shape_valid():
            self.shapes.append(self.trim_shape())
            for tup in self.inputButtons.keys():
                self.inputButtons[tup][1].config(background='white')
                self.inputButtons[tup][0] = False
                self.grid[tup[0]][tup[1]] = 0
            self.updateCount()


    def updateCount(self):
        self.shapeCount['text'] = f'{len(self.shapes)}'

    def trim_shape(self):
        outputMatrix = []

        # Trim the left side
        colVal = 0
        colValEnd = len(self.grid[0]) - 1
        for col in range(len(self.grid[0])):
            add = False
            tempCol = [row[col] for row in self.grid]
            for value in tempCol:
                if value == 1: add = True
            if not add:
                colVal += 1
            else:
                break

        # Trim the right side
        for col in range(len(self.grid[0]))[::-1]:
            tempCol = [row[col] for row in self.grid]
            add = False
            for value in tempCol:
                if value == 1: add = True
            if not add:
                colValEnd -= 1
            else:
                break

        for row in self.grid:
            add = False
            for value in row:
                if value == 1:
                    add = True
                    break
            if add: outputMatrix.append(row[colVal:colValEnd + 1])

        return outputMatrix


    def get_pos_and_vol(self):
        output = [False]
        volume = 0
        pos_found = False
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value and not pos_found:
                    output[0] = (i, j)
                    volume += 1
        output.append(volume)
        return output


    def determine_shape_valid(self):
        tuple = self.get_pos_and_vol()
        if tuple[0]:
            pos = tuple[0]
            vol = tuple[1]

            return self.calculate_volume(pos) == vol
        else: return False


    def calculate_volume(self, pos):
        dupes = {pos: True}
        stack = [pos]
        counter = 0
        while len(stack) > 0:
            tempPos = stack.pop()
            counter += 1

            # Check down
            if (tempPos[0] + 1, tempPos[1]) not in dupes and tempPos[0] + 1 < len(self.grid) \
                    and self.grid[tempPos[0] + 1][tempPos[1]] == 1:
                stack.append((tempPos[0] + 1, tempPos[1]))
                dupes[(tempPos[0] + 1, tempPos[1])] = True

            # Check up
            if (tempPos[0] - 1, tempPos[1]) not in dupes and tempPos[0] - 1 >= 0 \
                    and self.grid[tempPos[0] - 1][tempPos[1]] == 1:
                stack.append((tempPos[0] - 1, tempPos[1]))
                dupes[(tempPos[0] - 1, tempPos[1])] = True

            # Check to the right
            if (tempPos[0], tempPos[1] + 1) not in dupes and tempPos[1] + 1 < len(self.grid[0]) \
                    and self.grid[tempPos[0]][tempPos[1] + 1] == 1:
                stack.append((tempPos[0], tempPos[1] + 1))
                dupes[(tempPos[0], tempPos[1] + 1)] = True

            # Check to the left
            if (tempPos[0], tempPos[1] - 1) not in dupes and tempPos[1] - 1 >= 0 \
                    and self.grid[tempPos[0]][tempPos[1] - 1] == 1:
                stack.append((tempPos[0], tempPos[1] - 1))
                dupes[(tempPos[0], tempPos[1] - 1)] = True

        return counter


    def show_shapes(self):
        for i, shape in enumerate(self.shapes):
            print('#####################')
            print(f'This is shape number: {i + 1}')
            for row in shape:
                print(row)


    def run(self):
        self.root.mainloop()
