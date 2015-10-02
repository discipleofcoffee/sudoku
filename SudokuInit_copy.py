__author__ = 'Kshitij'

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
"""

import socket

def cellPlaceLocator():
    index = 0
    cellPlace = {}
    for rows in range(0,9):
        for cols in range(0,9):
            cellPlace[(rows,cols)] = index
            index += 1
    return cellPlace

locTranslat = cellPlaceLocator()

class SudokuParser(object):
    """ Accepts a string and parses into a sudoku puzzle table and the sub-boxes.

    :param sudokuString: Accepts a string representative of the sudoku puzzle.
    """

    def __init__(self, sudokuString):
        self.sudokuString = sudokuString
        self.sudokuTable = []
        self.puzzleAsListDict = {}

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

    def makePuzzleAsListDict(self):


        sudokuRows = self.sudokuString.split('\n')
        self.puzzleAsListDict = []
        for rows in range(0,9):
            for cols in range(0,9):
                boxLoc = self.boxLoc(rows, cols)
                val = (sudokuRows[rows][cols])
                origVal = (val,)
                mutable = True
                if val != '0':
                    mutable = False

                rowColBox = (rows, cols, boxLoc)

                self.puzzleAsListDict.append({'rowColBox': rowColBox, 'val': val, 'origVal': origVal, 'mutable': mutable})
        return self.puzzleAsListDict

    def sudokuTabulate(self):
        """ Converts the sudoku puzzle string into a list of lists to mimic a table structure.
        """

        sudokuRows = self.sudokuString.split('\n')
        for rowStrings in sudokuRows:
            self.sudokuTable.append(list(rowStrings))
        return self.sudokuTable

    def makePuzzleAsString(self, puzzleAsListDict):
        """ Converts the puzzle in a grid-puzzle string form.
        """

        puzzleAsString = []
        for element in puzzleAsListDict:
            puzzleAsString.append(element['val'])
            if element['rowColBox'][1] == 8 and element['rowColBox'][0] != 8:
                puzzleAsString.append('\n')

        return ''.join(puzzleAsString)




class SudokuSolver(object):

    def __init__(self, sudokuElements):

        elems = sudokuParser.sudokuElem



    def considerRow(self,rowNum):
        pass

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

def setValue(puzzleAsListDict, newVal, elemRow, elemCol):
    """ setter function to change values in cell safely
    :param puzzleAsListDict: list of dict, the puzzle to be solved
    :param newVal: int, new value to replace the old one.
    :param elemRow: int, Row number of the cell to be changed
    :param elemCol: int, Column number of the cell to be changed
    :return: list of dict
    """

    currentIdx = locTranslat{(elemRow, elemCol)}
    if puzzleAsListDict[currentIdx]['mutable']:
        puzzleAsListDict[currentIdx]['val'] = newVal
    else:
        print('Error: Value immutable:', puzzleAsListDict[currentIdx])
    return puzzleAsListDict




#    puzzleAsListDict[]




if __name__ == '__main__':

    """
    parse the sudoku into rows columns and blocks.
    Also, give each of them a unique place.
    then work at first cell, and consider all rows columns and blocks in it.
    start filling out.

    """

    puzzlePath = setPath()
    sudokuString = getPuzzle(puzzlePath, puzzleFileName = 'SudokuInitPuzzleF2.csv')

    sudokuPuzzle = SudokuParser(sudokuString)
    table = sudokuPuzzle.sudokuTabulate()
    elems = sudokuPuzzle.makePuzzleAsListDict()
    puzzleString = sudokuPuzzle.makePuzzleAsString(elems)
    print(sudokuString == puzzleString)
    print(puzzleString,'\n')
    print(sudokuString)
    pass








