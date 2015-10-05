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


class CellContext(object):

    @staticmethod
    def indexOfCell():
        index = 0
        cellPlace = {}
        for rows in range(0,9):
            for cols in range(0,9):
                cellPlace[(rows,cols)] = index
                index += 1
        return cellPlace

    @staticmethod
    def rowOfIndex():
        rowPlace = {}
        for rows in range(0, 9):
            rowPlace[rows] = [elem+(rows*9) for elem in list(range(0, 9, 1))]
        return rowPlace

    @staticmethod
    def colOfIndex():
        colPlace = {}
        for cols in range(0,9):
            colPlace[cols] = [elem+cols for elem in list(range(0, 81, 9))]
        return colPlace

    @staticmethod
    def boxOfIndex():
        boxPlace = {}
        boxCount = 0
        for rowBlock in range(0,3):
            for colCount in range(0,9,3):
                boxTemp = []
                for rowCount in range(0+3*rowBlock,3+3*rowBlock):
                    boxTemp.extend(cellRow[rowCount][colCount:colCount+3])
                boxPlace[boxCount] = set(boxTemp)
                boxCount += 1
        return boxPlace




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


class SudokuPuzzle(object):
    """ Sudoku Puzzle custom data type. Accepts a string and parses into a sudoku puzzle list of dict for solcing and
        view it as puzzle grid.

    :param sudokuString: Accepts a string representative of the sudoku puzzle.
    """

    def __init__(self, puzzleInputString):
        self.puzzleInputString = puzzleInputString
        self.sudokuTable = []
        self.puzzleAsList = {}

    def boxLoc(self, rowNum, colNum):
        """ Determines sub-box location based on row and column number.
        :param rowNum: int, row number
        :param colNum: int, column number
        :return: str
        """

        if rowNum in range(0,3):
            boxRowLoc = 't'
        elif rowNum in range(3,6):
            boxRowLoc = 'm'
        elif rowNum in range(6,9):
            boxRowLoc = 'b'

        if colNum in range(0,3):
            boxColLoc = 'l'
        elif colNum in range(3,6):
            boxColLoc = 'm'
        elif colNum in range(6,9):
            boxColLoc = 'r'

        return boxRowLoc + boxColLoc

    def makePuzzleAsList(self):


        sudokuRows = self.puzzleInputString.split('\n')
        self.puzzleAsList = []
        for rows in range(0,9):
            for cols in range(0,9):
                boxLoc = self.boxLoc(rows, cols)
                val = (sudokuRows[rows][cols])
                origVal = (val,)
                mutable = True
                if val != '0':
                    mutable = False

                rowColBox = (rows, cols, boxLoc)

                self.puzzleAsList.append({'rowColBox': rowColBox, 'val': val, 'origVal': origVal, 'mutable': mutable, 'lastModded': False})
        return self.puzzleAsList

    def sudokuTabulate(self):
        """ Converts the sudoku puzzle string into a list of lists to mimic a table structure.
        """

        sudokuRows = self.puzzleInputString.split('\n')
        for rowStrings in sudokuRows:
            self.sudokuTable.append(list(rowStrings))
        return self.sudokuTable

    def getPuzzleAsList(self):
        return self.puzzleAsList

    def getPuzzle(self):
        """ Converts the puzzle in a grid-puzzle string form.
        """

        puzzleAsString = []
        for element in self.puzzleAsList:
            puzzleAsString.append(element['val'])
            if element['rowColBox'][1] == 8 and element['rowColBox'][0] != 8:
                puzzleAsString.append('\n')

        return ''.join(puzzleAsString)

    def setValue(self, newVal, elemRow, elemCol):
        """ setter function to change values in cell safely
        :param newVal: int, new value to replace the old one.
        :param elemRow: int, Row number of the cell to be changed
        :param elemCol: int, Column number of the cell to be changed
        :return: list of dict
        """

        currentIdx = cellIndex[(elemRow, elemCol)]
        if self.puzzleAsList[currentIdx]['mutable']:
            self.puzzleAsList[currentIdx]['val'] = newVal
        else:
            print('Error: Value immutable:', self.puzzleAsList[currentIdx])



class SudokuSolver(object):

    def __init__(self, puzzle):

        puzzleList = puzzle.getPuzzleAsList()
        colVals = {}


    def analyzeCell(self):
        pass

if __name__ == '__main__':

    """
    parse the sudoku into rows columns and blocks.
    Also, give each of them a unique place.
    then work at first cell, and consider all rows columns and blocks in it.
    start filling out.

    """

    cellIndex = CellContext.indexOfCell()
    cellRow = CellContext.rowOfIndex()
    cellCol = CellContext.colOfIndex()
    cellBox = CellContext.boxOfIndex()

    puzzlePath = setPath()
    sudokuString = getPuzzle(puzzlePath, puzzleFileName = 'SudokuInitPuzzleF2.csv')

    sudokuPuzzle = SudokuPuzzle(sudokuString)
    table = sudokuPuzzle.sudokuTabulate()
    elems = sudokuPuzzle.makePuzzleAsList()
    puzzleString = sudokuPuzzle.getPuzzle()
    print(sudokuString == puzzleString)
    print(puzzleString,'\n')
    print(sudokuString)
    pass








