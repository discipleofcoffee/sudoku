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


class SudokuParser(object):
    """ Accepts a string and parses into a sudoku puzzle table and the sub-boxes.

    :param sudokuString: Accepts a string representative of the sudoku puzzle.
    """

    def __init__(self, sudokuString):
        self.sudokuString = sudokuString
        self.sudokuTable = []
        self.sudokuElem = {}

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

    def setCellAttributes(self):


        sudokuRows = self.sudokuString.split('\n')
        self.sudokuElem = []
        for rows in range(0,9):
            for cols in range(0,9):
                boxLoc = self.boxLoc(rows, cols)
                val = int(sudokuRows[rows][cols])
                origVal = tuple(val)
                if val:
                    mutable = bool(1)
                else:
                    mutable = bool(0)
                rowColBox = (rows, cols, boxLoc)

                self.sudokuElem.append({'rowColBox': rowColBox, 'val': val, 'origVal': origVal, 'mutable': mutable})
        return self.sudokuElem

    def sudokuTabulate(self):
        """ Converts the sudoku puzzle string into a list of lists to mimic a table structure.
        """

        sudokuRows = self.sudokuString.split('\n')
        for rowStrings in sudokuRows:
            self.sudokuTable.append(list(rowStrings))
        return self.sudokuTable




class sudokuSolver(object):

    def __init__(self, sudokuElements):

        elems = sudokuParser.sudokuElem



    def considerRow(self,rowNum):
        



if __name__ == '__main__':

    """
    parse the sudoku into rows columns and blocks.
    Also, give each of them a unique place.
    then work at first cell, and consider all rows columns and blocks in it.
    start filling out.

    """

    sudokuPuzzleFile = open('C:\\Users\Kshitij\OneDrive\ProgrammingProjects\Python\Sudoku\SudokuInitPuzzleF2.csv', encoding='utf-8')
    sudokuString = sudokuPuzzleFile.read()

    sudokuPuzzle = SudokuParser(sudokuString)
    table = sudokuPuzzle.sudokuTabulate()
    elems = sudokuPuzzle.setCellAttributes()
    sudokuPuzzle.sudokuSubBoxer()








