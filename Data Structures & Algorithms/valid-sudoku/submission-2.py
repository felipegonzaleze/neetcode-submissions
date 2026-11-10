class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = 0
        num = 0
        starter_row = 0
        starter_col = 0
        boxes = defaultdict(set)
        while count != 81:
            for i in range(starter_row, starter_row + 3):
                for j in range(starter_col, starter_col + 3):
                    if board[i][j] in boxes[num]:
                        return False
                    if board[i][j] != ".":
                        boxes[num].add(board[i][j])
                    count += 1
            num += 1
            starter_col += 3
            if starter_col == 9:
                starter_row += 3
                starter_col = 0
 
        for i in range(9):
            col_set = set()
            row_set = set()
            for j in range(9):
                if board[j][i] in col_set or board[i][j] in row_set:
                    print(board[j][i], board[i][j])
                    return False
                if board[j][i] != ".":
                    col_set.add(board[j][i])
                if board[i][j] != ".":
                    row_set.add(board[i][j])

        return True