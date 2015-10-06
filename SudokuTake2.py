__author__ = 'Kshitij'


import socket

"""
058000000
006315890
710000503
060050300
582000471
007080060
104000036
073642100
000000740

!!!! I can create a sudoku variable (class) which can do all this.
"""


def setPath():
    """ Sets the path for the puzzle file depending on the system the program is run on.
    :return: str
    """
    if socket.gethostname() == 'HomeDesktop':
        puzzlePath = 'C://Users/KC/OneDrive/ProgrammingProjects/Python/Sudoku/'
    else:
        puzzlePath = 'C://Users/Kshitij/OneDrive/ProgrammingProjects/Python/Sudoku/'
    return puzzlePath

def getPuzzle(puzzlePath, puzzleFileName = 'SudokuInitPuzzleF2.csv'):
    """ Converts puzzle file into a string to be parsed
    :param puzzlePath: (type: str) puzzle file name's path
    :param puzzleFileName: (type: str) puzzle file's name. Default: 'SudokuInitPuzzleF2.csv'
    :return: str
    """
    sudokuPuzzleFile = puzzlePath
    sudokuPuzzleFile = open(puzzlePath+puzzleFileName, encoding='utf-8')
    sudokuString = sudokuPuzzleFile.read()
    return sudokuString

def puzzleRows(puzzleInputString):
    puzzleRows = puzzleInputString.split('\n')
    return puzzleRows

def puzzleCols(puzzleInputString):
    puzzleCols = []
    for colCount in range(0,9):
        puzzleCols.append([puzzleInputString[idx] for idx in range(colCount,89,10)])
    return puzzleCols
#
# def puzzleBox(puzzleInputString):
#     puzzleBoxes = []
#     for rowCount in range(0,9):
#         puzzleRows[rowCount][0:3]
#         puzzleBoxes.append([puzzleString[idx] for idx in range(boxCount,89,10)])
#     return puzzleBoxes
#
# for count in range(0,3):
#     list(range(0+count*10,3+count*10))
#
# boxIdx = []
# for boxCount in range(0,9):
#     boxBegin = 0
#     boxEnd = 3
#     boxIdxTemp = []
#     boxIdxTemp = ([list(range(boxBegin+count*10,boxEnd+count*10)) for count in range(0,3)])
#     boxIdx.append([item for subList in boxIdxTemp for item in subList])
#



if __name__ == '__main__':

    puzzlePath = setPath()
    puzzleString = getPuzzle(puzzlePath, puzzleFileName = 'SudokuInitPuzzleF2.csv')
    puzzleRows = puzzleRows(puzzleString)
    puzzleCols = puzzleCols(puzzleString)
    pass