from tkinter import *

def toggle_button(x,y):
    tempButton = buttons[(x,y)]
    if not tempButton[0]:
        tempButton[1].config(background='green')
        grid[x][y] = 1
        tempButton[0] = not tempButton[0]
    else:
        tempButton[1].config(background='white')
        grid[x][y] = 0
        tempButton[0] = not tempButton[0]

def clear_all():
    for tup in buttons.keys():
        buttons[tup][1].config(background='white')
        grid[tup[0]][tup[1]] = 0

def clear_and_add(x,y):
    pass

def trim_shape():
    outputMatrix = []

    # Trim the left side
    colVal = 0
    colValEnd = len(grid[0])-1
    for col in range(len(grid[0])):
        add = False
        tempCol = [row[col] for row in grid]
        for value in tempCol:
            if value == 1: add = True
        if not add: colVal += 1
        else: break

    # Trim the right side
    for col in range(len(grid[0]))[::-1]:
        tempCol = [row[col] for row in grid]
        add = False
        for value in tempCol:
            if value == 1: add = True
        if not add:
            colValEnd -= 1
        else:
            break

    for row in grid:
        add = False
        for value in row:
            if value == 1:
                add = True
                break
        if add: outputMatrix.append(row[colVal:colValEnd+1])

    print(f'Column value: {colVal} column end: {colValEnd}')
    for row in outputMatrix:
        print(row)
    print('#################')
    print('')
    return outputMatrix

def determine_shape_valid(pos, vol):
    return calculate_volume(pos) == vol

def calculate_volume(pos):
    dupes = {pos: True}
    stack = [pos]
    counter = 0
    while len(stack) > 0:
        tempPos = stack.pop()
        counter += 1

        # Check down
        if (tempPos[0] + 1, tempPos[1]) not in dupes and tempPos[0] + 1 < len(grid) \
                and grid[tempPos[0] + 1][tempPos[1]] == 1:
            stack.append((tempPos[0] + 1, tempPos[1]))
            dupes[(tempPos[0] + 1, tempPos[1])] = True

        # Check up
        if (tempPos[0] - 1, tempPos[1]) not in dupes and tempPos[0] - 1 >= 0 \
                and grid[tempPos[0] - 1][tempPos[1]] == 1:
            stack.append((tempPos[0] - 1, tempPos[1]))
            dupes[(tempPos[0] - 1, tempPos[1])] = True

        # Check to the right
        if (tempPos[0], tempPos[1] + 1) not in dupes and tempPos[1] + 1 < len(grid[0]) \
                and grid[tempPos[0]][tempPos[1] + 1] == 1:
            stack.append((tempPos[0], tempPos[1] + 1))
            dupes[(tempPos[0], tempPos[1] + 1)] = True

        # Check to the left
        if (tempPos[0], tempPos[1] - 1) not in dupes and tempPos[1] - 1 >= 0 \
                and grid[tempPos[0]][tempPos[1] - 1] == 1:
            stack.append((tempPos[0], tempPos[1] - 1))
            dupes[(tempPos[0], tempPos[1] - 1)] = True

    print(counter)
    return counter

root = Tk()

shapeInput = Frame(root, padx=50, pady=50)
buttonFrame = Frame(shapeInput, padx=20, pady=15)
buttons = dict()
grid = [[0 for _ in range(5)] for _ in range(5)]
for x in range(5):
    for y in range(5):
        tempButton = Button(buttonFrame, padx=10, pady=3, bg='white', command=lambda x=x, y=y: toggle_button(x,y))
        tempButton.grid(row=x, column=y)
        buttons[(x,y)] = [False, tempButton]


buttonFrame.grid(row=0, column=1, columnspan=5, rowspan=5)
Button(shapeInput, text='Reset', pady=3, padx=6, command=clear_all).grid(row=4, column= 0)
Button(shapeInput, text='Next', pady=3, padx=6, command=determine_shape_valid).grid(row=4, column= 6)
Button(shapeInput, text='Done', pady=3, padx=6, command=trim_shape).grid(row=5, column=6)

# Feedback section
shapeFeedback = Frame(shapeInput, borderwidth=2, relief='groove')
Label(shapeFeedback, text='Result:').grid(row=0, column=0)
feedbackLabel = Label(shapeFeedback, text='text').grid(row=0, column=1)
shapeFeedback.grid(row=5, column=0, columnspan=6)


shapeInput.pack()

s = [1,2,3,4,5,6]

root.mainloop()





s = [
    [1,0,0,0],
    [1,0,1,0],
    [0,1,0,1],
    [0,1,1,1]
]






