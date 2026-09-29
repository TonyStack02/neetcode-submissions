class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_dict = {}

        for i in range (9):
            sudoku_dict["R"+str(i)]=set()
            sudoku_dict["C"+str(i)]=set()

        for i in range(3):
            for j in range (3):
                sudoku_dict["B"+str(i)+str(j)]=set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in sudoku_dict["R"+str(i)]:
                        return False
                    else:
                        sudoku_dict["R"+str(i)].add(board[i][j])

                    if board[i][j] in sudoku_dict["C"+str(j)]:
                        return False
                    else:
                        sudoku_dict["C"+str(j)].add(board[i][j])

                    if board[i][j] in sudoku_dict["B"+str(i//3)+str(j//3)]:
                        return False
                    else:
                        sudoku_dict["B"+str(i//3)+str(j//3)].add(board[i][j])
        return True