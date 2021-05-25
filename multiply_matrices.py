# Le7Sel
# multiply 2 matrices together
from tkinter import *

def multMatrix(m1, m2):
    result = [[0 for x in range(len(m2[0]))] for y in range(len(m1))]
    for x in range(len(m2[0])):
        for y in range(len(m1)):
            for i in range(len(m2)):
                result[y][x] += m1[y][i] * m2[i][x]
    return result

def makeMatrix(parent, height, width, padding, content='empty', packDir='Left' ):
    mat = Frame(parent)
    if (packDir == 'Left'):
        mat.pack(side = LEFT)
    else:
        mat.pack()
    rows = []
    Result = [[] for x in range(height)]

    for y in range(height):
        row = Frame(mat, padx=padding, pady=padding)
        rows.append(row)
        row.pack()
        for x in range(width):
            if content=='empty':
                label = Entry(rows[y], width=4)
                Result[y].append(label)
                label.pack(side=LEFT)
            else:
                label = Label(rows[y], text='', padx = padding, pady = padding)
                Result[y].append(label)
                label.pack(side=LEFT)

    return Result

def readMat(mat):
    return [[int(mat[y][x].get()) for x in range(len(mat[0]))] for y in range(len(mat))]

def writeMat(dest, mat):
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            dest[y][x].configure(text=str(mat[y][x]))

def equal():
    writeMat(resultMat, multMatrix(readMat(mat1), readMat(mat2)))


mat1Y = int(input('How many rows does the first matrice have? : '))
mat1X = int(input('How many columns does the first matrice have? : '))
mat2Y = int(input('How many rows does the second matrice have? : '))
mat2X = int(input('How many columns does the second matrice have? : '))

if (mat1X == mat2Y):
    root = Tk()
    root.title("Multiply Matrices")

    pad=10

    mat1 = makeMatrix(root, mat1Y, mat1X, pad)
    Label(root, text="x").pack(side=LEFT)
    mat2 = makeMatrix(root, mat2Y, mat2X, pad)
    Button(root, text='=', command=equal).pack(side=LEFT)
    resultMat = makeMatrix(root, mat1Y, mat2X, pad, 'result')
    root.mainloop()
else:
    print("These matrices cannot be multiplied")


