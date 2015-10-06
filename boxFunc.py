__author__ = 'KC'

puzzleString = ['058000000\n006315890\n710000503\n060050300\n582000471\n007080060\n104000036\n073642100\n000000740']
puzzleRows = ['058000000', '006315890', '710000503', '060050300', '582000471', '007080060', '104000036', '073642100', '000000740']
puzzleCols = [['0', '0', '7', '0', '5', '0', '1', '0', '0'], ['5', '0', '1', '6', '8', '0', '0', '7', '0'], ['8', '6', '0', '0', '2', '7', '4', '3', '0'], ['0', '3', '0', '0', '0', '0', '0', '6', '0'], ['0', '1', '0', '5', '0', '8', '0', '4', '0'], ['0', '5', '0', '0', '0', '0', '0', '2', '0'], ['0', '8', '5', '3', '4', '0', '0', '1', '7'], ['0', '9', '0', '0', '7', '6', '3', '0', '4'], ['0', '0', '3', '0', '1', '0', '6', '0', '0']]
#
# boxIdx = []
# boxBegin = 0
# boxEnd = 3
# for boxCount in range(0,3):
#     boxIdxTemp = []
#     boxIdxTemp = ([list(range(boxBegin+count*10,boxEnd+count*10)) for count in range(0,3)])
#     print(boxIdxTemp)
#     boxIdx.append([item for subList in boxIdxTemp for item in subList])
#     print(boxIdx)
#     boxBegin += 3*(boxCount+1)
#     boxEnd += 3*(boxCount+1)
# pass
pass
puzzleBox = []


for rowBlockStart in range(0,9,3):
    for colBlockStart in range(0,9,3):
        puzzleBoxTemp = []
        for rowCount in range(rowBlockStart,rowBlockStart+3):
            puzzleBoxTemp.append(puzzleRows[rowCount][colBlockStart:colBlockStart+3])
        puzzleBoxTemp = ''.join(puzzleBoxTemp)
        puzzleBox.append(puzzleBoxTemp)
#row block 0:3,col block 0:3
# puzzleRows[row0][col0,1,2]
# puzzleRows[row1][col0,1,2]
# puzzleRows[row2][col0,1,2]

#row block 0:3,col block 3:6
# puzzlerow[row0][col3,4,5]
# puzzlerow[row1][col3,4,5]
# puzzlerow[row2][col3,4,5]

#row block 0:3,col block 6:9
# puzzlerow[row0][col6,7,8]
# puzzlerow[row1][col6,7,8]
# puzzlerow[row2][col6,7,8]


#row block 3:6,col block 0:3
# puzzleRows[row3][col0,1,2]
# puzzleRows[row4][col0,1,2]
# puzzleRows[row5][col0,1,2]

#row block 3:6,col block 3:6
# puzzlerow[row3][col3,4,5]
# puzzlerow[row4][col3,4,5]
# puzzlerow[row5][col3,4,5]
